#!usr/bin/env python3
"""Fabric script generates .tgz archive of all in web_static"""
from fabric.api import local, task
from time import strtime

@task
def do_pack():
    """generate .tgz archive file with name 'versions' """
    timenow = strtime("%Y%M%W%D%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_.tgz{}".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
