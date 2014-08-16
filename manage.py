#!/usr/bin/env python3
import os
import sys

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

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_dellelce_net.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
