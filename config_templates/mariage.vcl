# This is a basic VCL configuration file for varnish.  See the vcl(7)
# man page for details on VCL syntax and semantics.
# 
# Default backend definition.  Set this to point to your content
# server.
# 
backend dealguru {
     .host = "127.0.0.1";
     .port = "41894";
}

acl purge {
        "localhost";
}

sub vcl_recv {
    # Purge everything url - this isn't the squid way, but works
    if (req.url ~ "^/varnishpurge") {
       if (!client.ip ~ purge) {
            error 405 "Not allowed.";
       }
       if (req.url == "/varnishpurge") {
            ban("req.http.host == " + req.http.host + " && req.url ~ ^/");
            error 841 "Purged site.";
       }
       else {
            ban("req.http.host == " + req.http.host + " && req.url ~ ^" + regsub( req.url, "^/varnishpurge(.*)$", "\1" ) + "$" );
            error 842 "Purged page.";
       }
    }
    
    if (req.request == "POST"){
    	return(pass);
    }
    
    # click registers are never cached.
    if (req.url ~ "^/register") {
        return(pass);
    }
    
    # allow PURGE from localhost and 192.168.55...
    if (req.request == "PURGE") {
        if (!client.ip ~ purge) {
            error 405 "Not allowed.";
        }
        return(lookup);
    }

    # unless sessionid/csrftoken is in the request, don't pass ANY cookies (referral_source, utm, etc)
    if (req.request == "GET" && (req.url ~ "^/static" || req.url ~ "^/api" || (req.http.cookie !~ "sessionid" && req.http.cookie !~ "csrftoken"))) {
        unset req.http.Accept-Encoding;
        unset req.http.Cookie;
    }

    # normalize accept-encoding to account for different browsers
    # see: https://www.varnish-cache.org/trac/wiki/VCLExampleNormalizeAcceptEncoding
    if (req.http.Accept-Encoding) {
        if (req.http.Accept-Encoding ~ "gzip") {
            set req.http.Accept-Encoding = "gzip";
        } elsif (req.http.Accept-Encoding ~ "deflate") {
            set req.http.Accept-Encoding = "deflate";
        } else {
            # unknown algorithm  
            unset req.http.Accept-Encoding;
        }
    }
    
    # Remove user agent
    if (req.http.User-Agent){
    	set req.http.User-Agent = "";
    }
   
    # look up the cache
    return(lookup);
}

sub vcl_hit {
	if (req.request == "PURGE") {
    	purge;
        error 200 "Purged (hit)";
    }
}

sub vcl_miss {
	if (req.request == "PURGE") {
    	purge;
        error 200 "Purged (miss)";
    }
}

sub vcl_fetch {
	# cache period (ttl: time to live)
    set beresp.ttl = 1h;
    # cache grace period; serve dirty
    set beresp.grace = 12h;
    
    # static files always cached 
    if (req.url ~ "^/static" || req.url ~"^/api/.*/deal_\w{2}/$") {
       unset beresp.http.set-cookie;
       return(deliver);
    }

    # pass through for anything with a session/csrftoken set
    if (beresp.http.set-cookie ~ "sessionid" || beresp.http.set-cookie ~ "csrftoken") {
       return(hit_for_pass);
    } else {
       return(deliver);
    }
}


sub vcl_deliver {
	if (obj.hits > 0) {
    	set resp.http.X-Cache = "HIT";
    } else {
        set resp.http.X-Cache = "MISS";
    }
}
