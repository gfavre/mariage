from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from cmsplugin_contact.cms_plugins import ContactPlugin
from models import CustomContact
from forms import RSVPForm

class RSVPContactPlugin(ContactPlugin):
    name = _("RSVP Form")
    
    model = CustomContact
    contact_form = RSVPForm
    
    # We're using the original cmsplugin_contact templates here which
    # works fine but requires that the original plugin is in INSTALLED_APPS.
    render_template = "rsvp/rsvp.html"
    email_template = "cmsplugin_contact/email.txt"
    
    fieldsets = (
        (None, {
                'fields': ('site_email', 'name_label', 'presence_label',
                           'content_label', 'thanks', 'submit'),
        }),
        (_('Spam Protection'), {
                'fields': ('spam_protection_method', 'akismet_api_key',
                           'recaptcha_public_key', 'recaptcha_private_key',
                           'recaptcha_theme')
        })
    )

plugin_pool.register_plugin(RSVPContactPlugin)