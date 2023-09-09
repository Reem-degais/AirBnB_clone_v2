#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Fabric script that generates a .tgz archive"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    files = "versions/web_static_{}.tgz".format(date)
    arc = local("sudo tar -cvzf {} web_static".format(files))
    if arc.succeeded:
        return files
    else:
        return None
