#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py
that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import run, put, env
import os


def do_deploy(archive_path):
    """ Uncompresses and deploy the archive into the servers """

    env.hosts = ['3.238.99.98', '34.207.154.242']
    if os.path.exists(archive_path) is False:
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/tmp')
        run('sudo mkdir -p {}'.format(dest))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('sudo rm -f /tmp/{}.tgz'.format(name))
        run('sudo mv {}/web_static/* {}/'.format(dest, dest))
        run('sudo rm -rf {}/web_static'.format(dest))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False
