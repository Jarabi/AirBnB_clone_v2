#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import run, put, env
from fabric.contrib import files
import os

# Define hosts and user
env.hosts = ['54.166.147.155', '54.237.127.172']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distributes an archive to web servers

    Args:
        archive_path: Path to where the archive is stored locally

    Returns:
        True: If all operations have been done correctly
        False: If any operation fails, like if archive_path doesn't exist
    """
    # Make sure archive path exists
    if os.path.isfile(archive_path) is False:
        return False

    try:
        # Get archive file (without leading path)
        archive_file = os.path.basename(archive_path)

        # Get folder name
        folder = archive_file.split('.')[0]

        # Extraction path (where archive will be extracted)
        extract_path = f"/data/web_static/releases/{folder}"

        # Upload the archive to /tmp/ folder of remote server
        put(archive_path, f"/tmp/{archive_file}")

        # Create folder in remote server
        run(f"mkdir -p {extract_path}")

        # Uncompress the archive to the folder /data/web_static/releases
        run(f"tar -xzf /tmp/{archive_file} -C {extract_path}/")

        # Delete the archive from remote server
        run(f"sudo rm /tmp/{archive_file}")

        # Move extracted content to new folder
        if files.exists(extract_path) is False:
            run(f"mv {extract_path}/web_static/* {extract_path}/")

        # Remove extracted folder (web_static) in remote server
        run(f"sudo rm -rf {extract_path}/web_static")

        # Delete symbolic link (/data/web_static/current) from remote server
        run('sudo rm -rf /data/web_static/current')

        # Create new symbolic link (/data/web_static/current)
        run(f"sudo ln -s {extract_path}/ /data/web_static/current")

        print("New version deployed!")

        return True
    except Exception:
        return False