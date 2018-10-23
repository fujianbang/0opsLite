#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import tornado.ioloop
import tornado.web

from tornado.options import define, options

from handlers.github_handler import GithubHandler

define("port", default=8000, help="run on the given port", type=int)
define("start", default=False, help="start server", type=bool)

def make_app():
    return tornado.web.Application([
        (r"/v1/github", GithubHandler),
    ])

if __name__ == "__main__":
    options.parse_command_line()

    if options.start:
        app = make_app()
        print "\033[0;32;40m【Tornado】正在监听端口{}...\033[0".format(options.port)
        app.listen(options.port)
        print "\033[0;32;40m【Tornado】服务已启动\033[0m"
        tornado.ioloop.IOLoop.current().start()
