# -*- coding: utf-8 -*-
"""
This fabfile deploys django apps on webfaction using gunicorn,
and supervisor.
"""
import os, re, xmlrpclib, sys, xmlrpclib, os.path, httplib

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import sed, exists, upload_template
from fabric.utils import abort
from fabric.context_managers import prefix, path
from fabric.operations import put

try:
    from fabsettings import WF_HOST, PROJECT_NAME, REPOSITORY, USER, PASSWORD, \
                            VIRTUALENVS, SETTINGS_SUBDIR, DBPASSWORD
except ImportError:
    print("ImportError: Couldn't find fabsettings.py, it either does not exist or giving import problems (missing settings)")
    sys.exit(1)


class WebFactionXmlRPC():
    def __init__(self, user, password):
        API_URL = 'https://api.webfaction.com/'
        try:
            http_proxy = os.environ['http_proxy']
        except KeyError:
            http_proxy = None
        self.server = xmlrpclib.Server(API_URL, transport=http_proxy)
        self.session_id, self.account = self.login(user, password)
    
    def login(self, user, password):
        return self.server.login(user, password)
    
    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            return getattr(self.server, name)(self.session_id, *args, **kwargs)
        return _missing


env.hosts             = [WF_HOST]
env.user              = USER
env.password          = PASSWORD
env.dbpassword        = DBPASSWORD
env.home              = os.path.join("/home/", USER)
env.project           = PROJECT_NAME
env.repo              = REPOSITORY
env.project_dir       = os.path.join(env.home, 'webapps', PROJECT_NAME)
env.settings_dir      = os.path.join(env.project_dir, SETTINGS_SUBDIR)
env.supervisor_dir    = os.path.join(env.home, 'webapps', 'supervisor')
env.virtualenv_dir    = VIRTUALENVS
env.virtualenv        = VIRTUALENVS + '/' + env.project
env.supervisor_ve_dir = os.path.join(env.virtualenv_dir, '/supervisor')
env.webfaction = WebFactionXmlRPC(USER, PASSWORD)



def bootstrap():
    "Initializes python libraries"
    run('mkdir -p %s/lib/python2.7' % env.home)
    run('easy_install-2.7 pip')
    run('pip-2.7 install virtualenv virtualenvwrapper')



def _create_db():
    print("Creating db...")
    db_name = '%s_%s' % (env.user, env.project)
    for db_info in env.webfaction.list_dbs():
        if db_info['name'] == db_name:
            return
    
    env.webfaction.create_db(db_name, 'postgresql', env.dbpassword)

def _create_static_app():
    print("Creating static app...")
    app_name = env.project + '_static'
    for app_info in env.webfaction.list_apps():
        if app_info['name'] == app_name:
            return
    
    env.webfaction.create_app(env.project + '_static', 'static_only', False, '')    


def _create_main_app():
    print("Creating main app...")
    app_name = env.project
    for app_info in env.webfaction.list_apps():
        if app_info['name'] == app_name:
            env.app_port = app_info['port']
            return
        
    port = env.webfaction.create_app(env.project, 'custom_app_with_port', False, '')
    
    
def configure_supervisor():
    print("Configuring supervisor...")
    if not 'app_port' in env:
    	for app_config in env.webfaction.list_apps():
    		if app_config.get('name') == env.project:
    			env.app_port = app_config.get('port')
    			break
    require('app_port')
    upload_template('config_templates/gunicorn.conf',
                    '%s/conf.d/%s.conf' % (env.supervisor_dir, env.project), env)

    reload_supervisor()
 
def configure_webfaction():
    _create_db()
    _create_static_app()
    _create_main_app()

def install_app():
    "Installs the django project in its own wf app and virtualenv"
    print("Grabbing sources...")
    configure_webfaction()
    with cd(env.home + '/webapps'):
        if not exists(env.project_dir + '/setup.py'):
            run('git clone %s %s' % (env.repo, env.project_dir))
    
    print("Creating virtualenv...")
    _create_ve(env.project)
    configure_supervisor()
            
    reload_app()
    restart_app()



def reload_app(arg=None):
    "Pulls app and refreshes requirements"
    with cd(env.project_dir):
        run('git pull pygreg master')
    
    if arg <> "quick":
        with cd(env.project_dir):
            #_ve_run(env.project, "pip install -r requirements.pip")
            #_ve_run(env.project, "pip install -e ./")
            djangoadmin('syncdb')
            djangoadmin('migrate')
            djangoadmin('collectstatic --noinput')
    
    restart_app()


def reload_supervisor():
    "Reload supervisor config"
    with cd(env.supervisor_dir):
        _ve_run('supervisor','supervisorctl reread && supervisorctl reload')

def restart_app():
    "Restarts the app using supervisorctl"
    with cd(env.supervisor_dir):            
        _ve_run('supervisor','supervisorctl restart %s' % env.project)




### Helper functions

def _create_ve(name):
    """creates virtualenv using virtualenvwrapper
    """
    if not exists(env.virtualenv_dir + '/name'):
        with cd(env.virtualenv_dir):
            run('mkvirtualenv -p /usr/local/bin/python2.7 --no-site-packages %s' % name)
    else:
        print("Virtualenv with name %s already exists. Skipping.") % name

def _ve_run(ve,cmd):
    """virtualenv wrapper for fabric commands
    """
    run("""source %s/%s/bin/activate && %s""" % (env.virtualenv_dir, ve, cmd))

def djangoadmin(cmd):
    _ve_run(env.project, "django-admin.py %s --settings=%s.settings" % (cmd, env.project))


def nero():
    try:
        env.webfaction.delete_app(env.project + '_static')
    except xmlrpclib.Fault, msg:
        print("Unable to delete static app (%s)") % msg
    try:
        env.webfaction.delete_app(env.project)
    except xmlrpclib.Fault, msg:
        print("Unable to delete main app (%s)") % msg
    
    try:
        db_name = '%s_%s' % (env.user, env.project)
        env.webfaction.delete_db(db_name, 'postgresql')
    except xmlrpclib.Fault, msg:
        print("Unable to delete db (%s)") % msg


def test():
    run("hostname")
    with cd(env.home + '/webapps'):
        if not exists(env.project_dir + '/setup.py'):
            run('git clone %s %s' % (env.repo, env.project_dir))
    
    put('config_templates/gunicorn.conf', '%s/conf.d/%s.conf' % (env.supervisor_dir, env.project))