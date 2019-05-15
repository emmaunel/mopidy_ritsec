import tornado.web as tw
import logging
import os


class RestartHandler(tw.RequestHandler):
    def post(self):
        self.write('{"message" : "System going down now!"}')
        logging.info("Web client rebooting....")
        os.system('reboot')