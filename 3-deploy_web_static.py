#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive
"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

created_archive = do_pack()


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    if created_archive is None:
        return False

    return do_deploy(created_archive)
