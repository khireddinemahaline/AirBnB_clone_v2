#!usr/bin/env python3
"""Fabric script generates .tgz archive of all in web_static"""
from fabric.api import local
from time import strtime
env.hosts = ['54.175.136.176','100.26.168.15']
env.user = 'ubuntu'


def do_pack():
    """generate .tgz archive file with name 'versions' """
    timenow = strtime("%Y%M%W%D%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None

def do_deploy(archive_path):
    """Deploy""""
    if not os.path.exists(archive_path):
        Return False
    try:
        filename = os.path.basename(archive_path)
        web_static_folder = filename.split('.')[0]

        releases_path = '/data/web_static/releases/{}'.format(web_static_folder)
        temp_path = '/tmp/{}'.format(filename)


        put(archive_path, temp_path)
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf {} -C {}'.format(temp_path, releases_path))


        run('rm {}'.format(temp_path))
        run('mv {}/web_static/* {}'.format(releases_path, releases_path))


        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))


        print('New version deployes!')
        return True
    except Exception as e:
        print('Error: {}'.format(e))
        Return False
