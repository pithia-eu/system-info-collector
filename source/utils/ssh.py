import os
import paramiko
from source.log.logger import logger


def create_ssh_client(ssh_host,
                      ssh_port,
                      ssh_user,
                      ssh_key_path):
    if not os.path.exists(ssh_key_path) or not os.path.isfile(ssh_key_path):
        logger.error(f'SSH key file does not exist at the given path: {ssh_key_path}')
        logger.info(f"Program exits with error")
        raise FileNotFoundError(f'SSH key file does not exist at the given path: {ssh_key_path}')
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        client.connect(ssh_host,
                       port=ssh_port,
                       username=ssh_user,
                       key_filename=ssh_key_path)
        logger.info('SSH client created')
        return client
    except paramiko.AuthenticationException:
        logger.exception("Authentication failed, please verify your credentials.",
                         exc_info=True)
        logger.info(f"Program exits with error")
        raise
    except paramiko.SSHException as e:
        logger.exception("Unable to establish SSH connection: {}".format(e),
                         exc_info=True)
        logger.info(f"Program exits with error")
        raise
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        logger.error("No valid connections could be established: {}".format(e))
        logger.info(f"Program exits with error")
        raise
    except Exception as e:
        logger.exception("Unexpected error: {}".format(e),
                         exc_info=True)
        logger.info(f"Program exits with error")
        raise

