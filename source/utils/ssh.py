import os
import paramiko
from source.log.logger import logger


def create_ssh_client(ssh_host,
                      ssh_port,
                      ssh_user,
                      ssh_key_path):
    if not os.path.exists(ssh_key_path) or not os.path.isfile(ssh_key_path):
        logger.error(f'SSH key file does not exist at the given path: {ssh_key_path}')
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
        raise
    except paramiko.SSHException as e:
        logger.exception("Unable to establish SSH connection: {}".format(e),
                         exc_info=True)
        raise
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        logger.error("No valid connections could be established: {}".format(e))
        raise
    except Exception as e:
        logger.exception("Unexpected error: {}".format(e),
                         exc_info=True)
        raise


def ssh_command(ssh_client,
                command,
                error_msg,
                info_msg):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command(command)
    exit_status = ssh_stdout.channel.recv_exit_status()
    if exit_status != 0:
        logger.error(f'{error_msg}: {ssh_stderr.read()}')
        raise Exception(f'{error_msg}: {ssh_stderr.read()}')
    else:
        result = ssh_stdout.read().decode('utf-8')
        logger.debug(f'{info_msg}: {result}')
        return result
