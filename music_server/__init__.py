import os.path
from mopidy import config, ext

__version__ = '0.1.1'


class Extension(ext.Extension):
    ext_name = 'music_server'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def setup(self, registry):
        # Change to tornado web stuff
        dirf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        registry.add('http:static', dict(name=self.ext_name, path=dirf))

# music_server = Flask(__name__)
#
# from music_server import routes
