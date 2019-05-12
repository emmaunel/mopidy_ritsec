from flask import Flask
import os.path
from mopidy import config, ext

class Extension(ext.Extension):
    ext_name = 'RITSEC Music'

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(config)


    def setup(self, registry):
        # Change to tornado web stuff
        dirf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        registry.add('http:static', dict(name=self.ext_name, path=dirf))

# app = Flask(__name__)
#
# from app import routes