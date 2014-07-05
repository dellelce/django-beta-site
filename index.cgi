#!/home/housefaq/i/bin/python3
#
# File:         index.cgi
# Created:      1658 050714
# Description:  demo site 
# Author:       Antonio Dell'Elce
#
# Based on: 
#    http://stackoverflow.com/questions/12658427/installing-a-django-site-on-godaddy
#
#

import os, sys, re
import logging 

## ENV ##

# django installation directory
installDir = "/home/housefaq/src/django"
sys.path.insert(0, installDir);


# thisPath: where this script is located
thisPath=os.path.dirname(os.path.realpath(__file__))
# confPath: where settings are located
basePath = os.path.basename(thisPath)
confPath = thisPath + "/" + basePath

sys.path.insert(0, thisPath);
sys.path.insert(0, confPath);

# our settings directory
os.environ['DJANGO_SETTINGS_MODULE'] = basePath + '.settings'

# for logging exceptions
try:
  serverName = os.environ['SERVER_NAME']
except:
  serverName = 'debug'

logging.basicConfig(filename='logs/' + serverName + '.log', level = logging.ERROR)

## MAIN ##

from django.core.signals import got_request_exception

#got_request_exception.connect(log)

from django.core.servers.fastcgi import runfastcgi

try:
  runfastcgi(method="threaded", daemonize="false")
except:
  logging.exception('uncaught')



## EOF ##
