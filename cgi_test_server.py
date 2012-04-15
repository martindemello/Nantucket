#!/usr/bin/python2

# simple cgi server example from
# http://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
import os
import glob
import shutil


# make the cgi directory
try:
    os.makedirs("cgi-bin")
except OSError:
    #directory already exists  
    pass

# copy all python files to cgi-bin
for filename in glob.glob("*.py"):
    shutil.copy(filename, "cgi-bin")

# start the server
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = server(server_address, handler)
httpd.serve_forever()
