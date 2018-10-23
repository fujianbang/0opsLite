#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def option(self):
        self.__set_response_header()

    def __set_response_header(self):
        self.set_header('content-type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, HEAD')
