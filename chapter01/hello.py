import  tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# tornado.options该模块用于从命令行中读取设置
from tornado.options import define,options
define("port", default=8000, help="run on the given port",type=int)

# 自己的web应用需要继承tornado.web.RequestHandler类
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # get_argument用于获取请求query字符串中的参数
        greeting = self.get_argument("greeting", "Hello")
        self.write(greeting+', tornado')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()