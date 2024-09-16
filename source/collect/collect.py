import scp
from source.log.logger import logger
from source.utils.environment import get_env_variable
from source.utils.ssh import create_ssh_client
from source.utils.directory import create_local_directory
from source.utils.permissions import change_local_directory_permission

BACKUP_FILE_PATTERN_ALL = "{backup_ssh_path}/{backup_dbname}_all_system_dbs_{timestamp}.{ext}"
BACKUP_FILE_PATTERN_DB = "{backup_ssh_path}/{backup_dbname}_db_{timestamp}.{ext}"


def generate_backup_file_paths(timestamp,
                               backup_dbname,
                               backup_ssh_path):
    return [
        BACKUP_FILE_PATTERN_ALL.format(backup_ssh_path=backup_ssh_path,
                                       backup_dbname=backup_dbname,
                                       timestamp=timestamp,
                                       ext="sql"),
        BACKUP_FILE_PATTERN_DB.format(backup_ssh_path=backup_ssh_path,
                                      backup_dbname=backup_dbname,
                                      timestamp=timestamp,
                                      ext="sql"),
        BACKUP_FILE_PATTERN_DB.format(backup_ssh_path=backup_ssh_path,
                                      backup_dbname=backup_dbname,
                                      timestamp=timestamp,
                                      ext="tar")
    ]


def generate_backup_command(backup_postgres_user,
                            backup_command,
                            backup_ssh_path):
    return f'sudo su {backup_postgres_user} -c "{backup_command} {backup_ssh_path}"'


def generate_backup_commands(timestamp,
                             backup_postgres_user,
                             backup_dbname,
                             backup_ssh_path):
    backup_files = generate_backup_file_paths(timestamp,
                                              backup_dbname,
                                              backup_ssh_path)
    backup_commands = {
        "dumpall": f"pg_dumpall -U {backup_postgres_user} -f",
        "dump": f"pg_dump -d {backup_dbname} -f",
        "dump_tar": f"pg_dump -d {backup_dbname} -F tar -f"
    }

    return [
        generate_backup_command(backup_postgres_user,
                                backup_commands['dumpall'],
                                backup_files[0]),
        generate_backup_command(backup_postgres_user,
                                backup_commands['dump'],
                                backup_files[1]),
        generate_backup_command(backup_postgres_user,
                                backup_commands['dump_tar'],
                                backup_files[2])
    ]


def is_true(env_variable):
    if env_variable.upper() == 'TRUE':
        return True
    else:
        return False


def collect_hostname(host_ssh_client, test):
    logger.debug('Collecting Hostname..')
    if test:
        return "test_hostname"

def collect_date(host_ssh_client, test):
    logger.debug('Collecting Date..')
    if test:
        return "test_date"

def collect_disks(host_ssh_client, test):
    logger.debug('Collecting Disk..')
    if test:
        return "test_disk"

def collect_updates(host_ssh_client, test):
    logger.debug('Collecting Updates..')
    if test:
        return "test_update"

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
    items_to_collect_list = [{"hostname":{"enabled":collect_hostname_bool, "function":collect_hostname}},
                             {"date":{"enabled":collect_date_bool, "function":collect_date}},
                             {"disks":{"enabled":collect_disks_bool, "function":collect_disks}},
                             {"updates":{"enabled":collect_updates_bool, "function":collect_updates}}]
    ssh_host_list = list(set(ssh_hosts.split(','))) if ssh_hosts else []
    collected_info_dict = {}
    for host in ssh_host_list:
        collected_info_dict[host] = {}
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
