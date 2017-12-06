import textwrap

import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web

from tornado.options import options,define
define("port", default=8000, help='run on the given port', type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, str):
        self.write(str[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))
    # 重写错误方法
    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error." % status_code)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/reverse/(\w+)', ReverseHandler),
            (r'/wrap', WrapHandler),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()




