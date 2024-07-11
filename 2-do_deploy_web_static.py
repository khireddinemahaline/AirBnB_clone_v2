#!usr/bin/env python3
"""
A function for deploying web_static content to web servers.
"""
from fabric.api import env, run, put
from datetime import datetime
import shlex
import os

env.hosts = []
env.user = ''


def do_deploy(archive_path):
    """d""""
    if not os.path.exists(archive_path):
        Return False
    try:
        filename = os.path.basename(archive_path)
        web_static_folder = filename.split('.')[0]

        release_path = '/data/web_static/releases/{}'.format(web_static_folder)
        temp_path = '/tmp/{}'.format(filename)


        put(archive_path, temp_path)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf {} -C {}'.format(temp_path, release_path))


        run('rm {}'.format())
