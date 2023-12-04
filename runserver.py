#!/usr/bin/env python

"""
author : Vinay Kumar Kuresi
created Date : 03/12/2023

"""


from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from settings import config
from auth_system import app


app.secret_key = config.SECRET_KEY
app.debug = True
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(80)
IOLoop.instance().start()

#app.run(host='0.0.0.0', port=8000)
