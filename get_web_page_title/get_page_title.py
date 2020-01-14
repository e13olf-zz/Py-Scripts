#!/usr/bin/python3

import urllib.request as ur
import re

chars = ",'[]"
file = open("urls.txt", "r")
urls = ''.join(c for c in file.read() if c not in chars)
urls = urls.split()
pattern = '<title>(.+?)</title>'
result = re.compile(pattern)
for url in urls:
	htmlsourcecode = ur.urlopen(url)
	htmltext = htmlsourcecode.read().decode('iso8859-1')    #https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s
	title = re.findall(result,htmltext)
	print(title)
