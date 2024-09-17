from source.collect.collect import is_true
from source.collect.commands import (collect_hostname,
                                     collect_uptime,
                                     collect_date,
                                     collect_os,
                                     collect_kernel,
                                     collect_os_disk,
                                     collect_ip,
                                     collect_firewall,
                                     collect_ports,
                                     collect_users,
                                     collect_groups,
                                     collect_services,
                                     collect_processes,
                                     collect_scheduled_tasks,
                                     collect_packages,
                                     collect_updates)
from source.utils.environment import get_env_variable


def get_items_to_collect():
    collect_hostname_bool = is_true(get_env_variable("COLLECT_HOSTNAME"))
    collect_uptime_bool = is_true(get_env_variable("COLLECT_UPTIME"))
    collect_date_bool = is_true(get_env_variable("COLLECT_DATE"))
    collect_os_bool = is_true(get_env_variable("COLLECT_OS"))
    collect_kernel_bool = is_true(get_env_variable("COLLECT_KERNEL"))
    collect_os_disk_bool = is_true(get_env_variable("COLLECT_OS_DISK"))
    collect_ip_bool = is_true(get_env_variable("COLLECT_IP"))
    collect_firewall_bool = is_true(get_env_variable("COLLECT_FIREWALL"))
    collect_ports_bool = is_true(get_env_variable("COLLECT_PORTS"))
    collect_users_bool = is_true(get_env_variable("COLLECT_USERS"))
    collect_groups_bool = is_true(get_env_variable("COLLECT_GROUPS"))
    collect_services_bool = is_true(get_env_variable("COLLECT_SERVICES"))
    collect_processes_bool = is_true(get_env_variable("COLLECT_PROCESSES"))
    collect_scheduled_tasks_bool = is_true(get_env_variable("COLLECT_SCHEDULED_TASKS"))
    collect_packages_bool = is_true(get_env_variable("COLLECT_PACKAGES"))
    collect_updates_bool = is_true(get_env_variable("COLLECT_UPDATES"))
    items_to_collect_list = [{"name": {"enabled": collect_hostname_bool,
                                       "function": collect_hostname}},
                             {"uptime": {"enabled": collect_uptime_bool,
                                         "function": collect_uptime}},
                             {"date": {"enabled": collect_date_bool,
                                       "function": collect_date}},
                             {"os": {"enabled": collect_os_bool,
                                     "function": collect_os}},
                             {"kernel": {"enabled": collect_kernel_bool,
                                         "function": collect_kernel}},
                             {"disks": {"enabled": collect_os_disk_bool,
                                        "function": collect_os_disk}},
                             {"ip": {"enabled": collect_ip_bool,
                                     "function": collect_ip}},
                             {"firewall": {"enabled": collect_firewall_bool,
                                           "function": collect_firewall}},
                             {"ports": {"enabled": collect_ports_bool,
                                        "function": collect_ports}},
                             {"users": {"enabled": collect_users_bool,
                                        "function": collect_users}},
                             {"groups": {"enabled": collect_groups_bool,
                                         "function": collect_groups}},
                             {"services": {"enabled": collect_services_bool,
                                           "function": collect_services}},
                             {"processes": {"enabled": collect_processes_bool,
                                            "function": collect_processes}},
                             {"scheduled_tasks": {"enabled": collect_scheduled_tasks_bool,
                                                  "function": collect_scheduled_tasks}},
                             {"packages": {"enabled": collect_packages_bool,
                                           "function": collect_packages}},
                             {"updates": {"enabled": collect_updates_bool,
                                          "function": collect_updates}}]
    return items_to_collect_list
