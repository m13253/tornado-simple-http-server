#!/usr/bin/env python

import os
import sys
import time
import tornado.httpserver
import tornado.ioloop
import tornado.log
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self, path):
        if not path:
            path = '.'
        if not os.path.isdir(path):
            raise tornado.web.HTTPError(404)
        self.write('<html>\n<head><title>Index of ')
        escaped_title = tornado.web.escape.xhtml_escape(self.request.path)
        self.write(escaped_title)
        self.write('</title></head>\n<body>\n<h1>Index of ')
        self.write(escaped_title)
        self.write('</h1>\n<hr />\n<table>\n')
        for f in sorted([i for i in os.listdir(path) if not i.startswith('.')]):
            absf = os.path.join(path, f)
            if os.path.isdir(absf):
                f += '/'
            self.write('<tr><td><a href="')
            self.write(tornado.web.escape.url_escape(f))
            self.write('">')
            self.write(tornado.web.escape.xhtml_escape(f))
            self.write('</a></td><td>')
            lstat_result = os.lstat(absf)
            self.write(tornado.web.escape.xhtml_escape(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lstat_result.st_mtime))))
            self.write('</td><td align="right">')
            self.write(tornado.web.escape.xhtml_escape(str(lstat_result.st_size)))
            self.write('</td></tr>\n')
        self.finish('</table>\n<hr />\n<div>Powered by <a href="https://github.com/m13253/tornado-simple-http-server" target="_blank">TornadoSimpleHTTPServer</a></div></body>\n</html>\n')


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
        [
            ('/(.*/)', IndexHandler),
            ('/()', IndexHandler),
            ('/(.*)', tornado.web.StaticFileHandler, {'path': '.', 'default_filename': ''}),
        ],
        gzip=True,
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(listen_port, listen_address)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
