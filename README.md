TornadoSimpleHTTPServer
=======================

This is a simple HTTP server serving static files.

Usage
-----

`python -m TornadoSimpleHTTPServer` or `python TornadoSimpleHTTPServer.py`

You can pass one or two arguments. The last argument is the TCP port number to listen on. The other one, if exists, is the hostname to listen on.

Notes
-----

Unlike `python -m http.server`, TornadoSimpleHTTPServer can serve multiple connections concurrently thanks to [Tornado web framework](http://www.tornadoweb.org).

This software, released under [GNU General Public License version 3](COPYING), is provided **as is**, and comes with **absolutely no warranty**. This software may contain bugs which may cause damage including data loss or leakage of confidential data. Please use this software at your own risk.
