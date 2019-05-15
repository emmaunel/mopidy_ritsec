# Simple Mopidy web Client for CSEC Labs
#
# Author: Emmanuel Adewale

import os.path
from mopidy import config, ext

__version__ = '0.1'


class Extension(ext.Extension):
    ext_name = 'mopidy_ritsec'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        print("Setting up defaults schema")
        schema = super(Extension, self).get_config_schema()
        schema['web_host'] = config.Hostname(optional=True)
        schema['web_port'] = config.Port(optional=True)
        return schema

    def validate_environment(self):
        print("Validating")

    def setup(self, registry):
        registry.add('http:app', {'name': self.ext_name, 'factory': self.factory})

    def factory(self, config, core):
        from tornado.web import StaticFileHandler, RedirectHandler
        from .Handlers import RestartHandler
        path = os.path.join(os.path.dirname(__file__), 'static')
        return [
            (r'/(.*)', StaticFileHandler, {'path': path, 'default_filename': 'index.html'}),
            (r'/restart', RestartHandler),
            (r'/', RedirectHandler, {'url', 'index.html'})]
