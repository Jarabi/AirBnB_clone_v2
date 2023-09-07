#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
    """

    # Get current time to use in file name
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    # Archive name
    archive_name = f"versions/web_static_{current_time}.tgz"

    # Create archive
    local(f"tar -cvf {archive_name} ./web_static")

    return archive_name
