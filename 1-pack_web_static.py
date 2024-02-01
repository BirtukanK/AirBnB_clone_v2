#!/usr/bin/python3
""" defines fabric script to generate a .tgz archive"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """ a function to write a fabric script"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
