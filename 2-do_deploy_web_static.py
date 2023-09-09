#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""

from fabric.api import env, put, run
import datetime
from os.path import exists


env.hosts = ['3.84.238.135', '34.207.155.69']

def do_deploy(archive_path):
    """function that distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False

    filename = archive_path.split('/')[-1]
    untgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(untgz))
        run("tar -xzf {} -C {}/".format(tmp, untgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(untgz, untgz))
        run("rm -rf {}/web_static".format(untgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(untgz))
        return True
    except:
        return False
