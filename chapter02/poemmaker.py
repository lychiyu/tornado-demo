import os.path
import tornado.options
import tornado.web
import tornado.ioloop
import tornado.httpserver

from tornado.options import define, options
define(name='port', default=8000, help='run on the given port', type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2,made=verb,difference=noun3)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/poem', PoemPageHandler),
        ],
        # 设置模板路径
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        # 设置静态资源文件路径使用方法是：{{ static_url("style.css") }}
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()