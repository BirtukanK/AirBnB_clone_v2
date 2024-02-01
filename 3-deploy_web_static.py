#!/usr/bin/python3
""" a fabric script that creates and distributes an archive to web servers"""
from fabric.api import *
from os.path import exists
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['18.234.80.85', '52.87.216.243']


def deploy():
    """ this function creates abd distributes an archive"""
    new_path = do_pack()
    if exists(new_path) is False:
        return False
    new_archive = do_deploy(new_path)
    return new_archive
