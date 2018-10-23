#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import json
import logging
import tornado.web

from .base_handler import BaseHandler

logger = logging.getLogger(__name__)

class GithubHandler(BaseHandler):

    @tornado.web.asynchronous
    def get(self, args=None):
        result = [{
                'id': 'x342',
                'name': 'iCipher',
                'url': '',
                'desc': 'Based on vuejs for api managing',
                'developer': 'fujianbang0ops',
                'lastUpdate': '2018.10.22',
                'star': '32'
            }, {
                'id': 'x322',
                'name': '0opsLite',
                'url': '',
                'desc': '基于微信小程序的移动多渠道监控工具',
                'developer': 'fujianbang0ops',
                'lastUpdate': '2018.10.20',
                'star': '0'
            }]

        logger.info(result)
        self.finish(json.dumps(result))
