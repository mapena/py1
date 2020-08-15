#!/usr/bin/env python
import os, urllib.request, urllib.error, urllib.parse, webbrowser

print ("Content-type: text/html\n")

qs = os.environ['QUERY_STRING']
if 'firstname' in qs:
    name = qs.split('=')[1]
else:
    name = 'No Name Provided'

print ("<html>")
print ("<body>")
print ("<h1>Hello %s</h1>" % name)
print ("</pre>")
print ("</body>")
print ("</html>")