#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<i@binux.me>
#         http://binux.me
# Created on 2014-08-08 21:06:02

import time
from base import *

import requests
import re

class AboutHandler(BaseHandler):
    @tornado.web.addslash
    def get(self):
        user = self.current_user
        tpls = []
        url = "https://github.com/qiandao-today/templates/blob/master/about.md"
        
        res = requests.get(url, verify=False)
        if (res.status_code == 200):
            content = res.content.decode(res.encoding, 'replace')
            About_content = re.findall(r"<article([\w\W]+?)</article", content)[0]
            tpls_temp = re.findall(r"tr>([\w\W]+?)</tr", About_content)
            
            for cnt in range(1, len(tpls_temp)):
                tpl_temp = re.findall(r"center\">(.+?)</td", tpls_temp[cnt])
                apiurl = re.findall(r"href=\"(.+?)\"", tpl_temp[1])[0]
                example = re.findall(r">(.+?)<", tpl_temp[5])[0]
                
                tpls.append ({
                                "api":tpl_temp[0],
                                "url":apiurl,
                                "vars":tpl_temp[2],
                                "varsreq":tpl_temp[3],
                                "comments":tpl_temp[4],
                                "examples":example
                            })
                
        self.render('about.html', tpls=tpls)

handlers = [
        ('/about/?', AboutHandler),
        ]

