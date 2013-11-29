#!/usr/bin/env python

import os
import sys
import tornado.httpserver
import tornado.ioloop
import tornado.log
import tornado.web


def main():
    listen_address = ''
    listen_port = 8000
    try:
        if len(sys.argv) == 2:
            listen_port = int(sys.argv[2])
        elif len(sys.argv) == 3:
            listen_address = sys.argv[1]
            listen_port = int(sys.argv[2])
    except ValueError as e:
        raise ValueError('port must be a number between 0 and 65535')
    tornado.log.enable_pretty_logging()
    application = tornado.web.Application(
        [],
        gzip=True,
        static_path=os.getcwd(),
        static_url_prefix='/'
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(listen_port, listen_address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
