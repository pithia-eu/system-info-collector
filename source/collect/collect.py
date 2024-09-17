from source.collect.hostinfo import get_items_to_collect
from source.log.logger import logger
from source.utils.environment import get_env_variable
from source.utils.ssh import create_ssh_client


def is_true(env_variable):
    if env_variable.upper() == 'TRUE':
        return True
    else:
        return False


def collect_info(timestamp,
                 test=False):
    logger.info('Collecting System info from Remote Hosts..')
    ssh_key_path = get_env_variable("SSH_KEY_PATH")
    ssh_port = int(get_env_variable("SSH_PORT"))
    ssh_user = get_env_variable("SSH_USER")
    ssh_hosts = get_env_variable("SSH_HOSTS")

    items_to_collect_list = get_items_to_collect()
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


