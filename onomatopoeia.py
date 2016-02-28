#!/usr/bin/env python2.7

import sys
import os
from glob    import glob
from urllib2 import urlopen
import urllib
import re

url_base     = r'https://commons.wikimedia.org'
commons_base = r'https://upload.wikimedia.org/wikipedia/commons'
url          = r'{base}/wiki/General_phonetics'.format(base = url_base)
ogg_dir      = r'./ogg_files/'

re_ogg_link = re.compile('(/wiki/File:([^.]+)\.ogg)')
re_ogg_file = re.compile('({base}/([^>]*)/([^>]*)\.ogg)'.format(base = commons_base))

print 'Accessing {url}...'.format(url = url)
ogg_links = {}
# Read through base to find a link to the upload page of each file
for line in urlopen(url):
   ogg_match = re_ogg_link.search(line)
   if ogg_match:
      ogg_links[ogg_match.group(2)] =  '{base}{ogg_link}'.format(base = url_base, ogg_link = ogg_match.group(1))
      #print "Adding '{url}'".format(url = ogg_match.group(1))

if not ogg_links:
   "Error : Didn't find any files"
print "Done - Now searching for the ogg_files themselves"

# Create a directory for all audio files
if not os.path.isdir(ogg_dir):
   os.mkdir(ogg_dir)

# Read through each file's upload page to find the file itself
for ogg_link in ogg_links.keys():
   print 'Searching for ogg files in "{url}"'.format(url = ogg_links[ogg_link])
   for line in urlopen(ogg_links[ogg_link]):
      ogg_match = re_ogg_file.search(line) 
      if ogg_match:
         print r'Saving "{ogg_file}" as "./ogg_files/{filename}.ogg"'.format(ogg_file = ogg_match.group(1), filename = ogg_match.group(3).lower())
         ogg = urllib.URLopener()
         ogg.retrieve(ogg_match.group(1), './ogg_files/{filename}.ogg'.format(filename=ogg_match.group(3).lower()))
         break
      
      
