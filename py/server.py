from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from restfulAPI import app
from os import environ

if __name__ == "__main__":
	http_server = HTTPServer(WSGIContainer(app))
	http_server.bind(environ.get("PORT", 80))
	http_server.start(1)
	IOLoop.instance().start()