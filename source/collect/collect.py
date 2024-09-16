from source.log.logger import logger
from source.utils.environment import get_env_variable
from source.utils.ssh import create_ssh_client
from source.utils.ssh import ssh_command


def is_true(env_variable):
    if env_variable.upper() == 'TRUE':
        return True
    else:
        return False


def collect_hostname(host_ssh_client, test):
    logger.debug('Collecting Hostname..')
    if test:
        return "test_hostname"
    command = "hostname"
    ssh_command_out = ssh_command(host_ssh_client,command,
                        "Error while collecting hostname",
                         "Hostname collected")
    return ssh_command_out.strip()

def collect_date(host_ssh_client, test):
    logger.debug('Collecting Date..')
    if test:
        return "test_date"
    command = "date"
    ssh_command_out = ssh_command(host_ssh_client, command,
                                  "Error while collecting date",
                                  "Date collected")
    return ssh_command_out.strip()

def collect_disks(host_ssh_client, test):
    logger.debug('Collecting Disk..')
    if test:
        return "test_disk"
    command = "df -h"
    ssh_command_out = ssh_command(host_ssh_client, command,
                                  "Error while collecting OS disk space",
                                  "OS disk space collected")
    ssh_command_out_lines = ssh_command_out.splitlines()
    for line in ssh_command_out_lines:
        line_list = line.split(" ")
        processed_line = [item for item in line_list if item != ""]
        if '/' in processed_line:
            return " ".join(processed_line)

def collect_updates(host_ssh_client, test):
    logger.debug('Collecting Updates..')
    if test:
        return "test_update"
    command = "apt list --upgradable"
    ssh_command_out = ssh_command(host_ssh_client, command,
                                  "Error while collecting available updates",
                                  "Available updates collected")
    ssh_command_out_lines = ssh_command_out.splitlines()
    return ssh_command_out.split("\n")

def collect_info(timestamp,
                 test=False):
    logger.info('Collecting System info from Remote Hosts..')
    ssh_key_path = get_env_variable("SSH_KEY_PATH")
    ssh_port = int(get_env_variable("SSH_PORT"))
    ssh_user = get_env_variable("SSH_USER")
    ssh_hosts = get_env_variable("SSH_HOSTS")

    collect_hostname_bool = is_true(get_env_variable("COLLECT_HOSTNAME"))
    collect_date_bool = is_true(get_env_variable("COLLECT_DATE"))
    collect_disks_bool = is_true(get_env_variable("COLLECT_DISKS"))
    collect_updates_bool = is_true(get_env_variable("COLLECT_UPDATES"))
    items_to_collect_list = [{"host_name":{"enabled":collect_hostname_bool, "function":collect_hostname}},
                             {"host_date":{"enabled":collect_date_bool, "function":collect_date}},
                             {"host_disks":{"enabled":collect_disks_bool, "function":collect_disks}},
                             {"host_updates":{"enabled":collect_updates_bool, "function":collect_updates}}]
    ssh_host_list = list(set(ssh_hosts.split(','))) if ssh_hosts else []
    collected_info_dict = {}
    for host in ssh_host_list:
        collected_info_dict[host] = {}
        collected_info_dict[host]["run_date"] = timestamp
        if test:
            logger.warning(f"Test model enabled - Collecting info for host: {host} disabled")
        else:
            logger.info(f"Collecting info for host: {host}")
        try:
            host_ssh_client = create_ssh_client(host,
                                                ssh_port,
                                                ssh_user,
                                                ssh_key_path)
        except Exception as e:
            logger.error(f"Cannot connect to host: {host} - {e}")
            collected_info_dict[host]["error"] = f"Cannot connect to host: {host} - {e}"
            continue
        for item_to_collect_dict in items_to_collect_list:
            for item_to_collect, config in item_to_collect_dict.items():
                if config['enabled']:
                    collected_info_dict[host][item_to_collect] = config['function'](host_ssh_client, test)
        if test:
            logger.warning(f"Testing collecting info for host: {host} completed")
        else:
            logger.info(f"Collecting info for host: {host} completed")
        host_ssh_client.close()
    logger.info('Collecting System info from Remote Completed')
    return collected_info_dict
