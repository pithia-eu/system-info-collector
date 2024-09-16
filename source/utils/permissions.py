import os
import pwd
import grp
import getpass

from source.log.logger import logger


def change_local_directory_permission(directory):
    user = getpass.getuser()
    uid = pwd.getpwnam(user).pw_uid
    gid = grp.getgrnam(user).gr_gid
    logger.debug(f"Checking permissions to path: '{directory}' for user: '{user}'")
    if os.access(directory, os.R_OK | os.W_OK | os.X_OK):
        logger.debug(f"Read/write/execute access already granted at path: '{directory}' for user: '{user}'")
    else:
        logger.debug(f"Modifying permissions at path: '{directory}' for user: '{user}'")
        os.chown(directory, uid, gid)
        os.chmod(directory, 0o700)
        logger.debug("Permission granted")
