#!/usr/bin/python3
""" Fabric script that distributes an archive to web servers"""
from fabric.api import *
from os.path import exists
env.hosts = ['18.234.80.85', '52.87.216.243']


def do_deploy(archive_path):
    """ method that distributes an archive to both our servers"""
    if exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = "/data/web_static/releases/{}".format(filename.split('.')[0])
    # current = '/data/web_static/current'
    tmp = "/tmp/" + filename
    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}/".format(no_tgz))
    run("sudo tar -xzf {} -C {}/".format(tmp, no_tgz))
    run("sudo rm -r {}".format(tmp))
    run("sudo mv {}/web_static/* {}/".format(no_tgz, no_tgz))
    run("sudo rm -rf {}/web_static".format(no_tgz))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {}/ /data/web_static/current".format(no_tgz))
