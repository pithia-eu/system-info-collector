from source.log.logger import logger
from source.utils.ssh import ssh_command


def collect_hostname(host_ssh_client,
                     test):
    logger.debug('Collecting Hostname..')
    if test:
        return "test_hostname"
    command = "hostname"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting hostname",
                                  "Hostname collected")
    return ssh_command_out


def collect_uptime(host_ssh_client,
                   test):
    logger.debug('Collecting Uptime..')
    if test:
        return "test_uptime"
    command = "uptime"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting uptime",
                                  "Uptime collected")
    return ssh_command_out


def collect_date(host_ssh_client,
                 test):
    logger.debug('Collecting Date..')
    if test:
        return "test_date"
    command = "date"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting date",
                                  "Date collected")
    return ssh_command_out


def collect_os(host_ssh_client,
               test):
    logger.debug('Collecting OS version..')
    if test:
        return "test_os"
    command = "lsb_release -a"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting OS version",
                                  "OS version collected")
    return ssh_command_out


def collect_kernel(host_ssh_client,
                   test):
    logger.debug('Collecting Kernel Version..')
    if test:
        return "test_kernel"
    command = "uname -r"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting OS kernel version",
                                  "OS kernel version collected")
    return ssh_command_out


def collect_os_disk(host_ssh_client,
                    test):
    logger.debug('Collecting OS Disk..')
    if test:
        return "test_disk"
    command = "df -h"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting OS disk space",
                                  "OS disk space collected")
    return ssh_command_out
    # ssh_command_out_lines = ssh_command_out.splitlines()
    # for line in ssh_command_out_lines:
    #     line_list = line.split(" ")
    #     processed_line = [item for item in line_list if item != ""]
    #     if '/' in processed_line:
    #         return " ".join(processed_line)


def collect_ip(host_ssh_client,
               test):
    logger.debug('Collecting IP address..')
    if test:
        return "test_ip"
    command = "ip addr"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting IP address",
                                  "IP address collected")
    return ssh_command_out


def collect_firewall(host_ssh_client,
                     test):
    logger.debug('Collecting Firewall Status..')
    if test:
        return "test_firewall"
    command = "sudo ufw status"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting firewall status",
                                  "Firewall status collected")
    return ssh_command_out


def collect_ports(host_ssh_client,
                  test):
    logger.debug('Collecting Listening Ports..')
    if test:
        return "test_ports"
    command = "ss -tuln"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting listening ports",
                                  "Listening ports collected")
    return ssh_command_out


def collect_users(host_ssh_client,
                  test):
    logger.debug('Collecting OS Users..')
    if test:
        return "test_users"
    command = "cat /etc/passwd"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting OS users",
                                  "OS users collected")
    return ssh_command_out


def collect_groups(host_ssh_client,
                   test):
    logger.debug('Collecting OS User Groups..')
    if test:
        return "test_groups"
    command = "cat /etc/group"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting OS user groups",
                                  "OS user groups collected")
    return ssh_command_out


def collect_services(host_ssh_client,
                     test):
    logger.debug('Collecting Running Services..')
    if test:
        return "test_services"
    command = "systemctl list-units --type=service --state=running"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting running services",
                                  "Running services collected")
    return ssh_command_out


def collect_processes(host_ssh_client,
                      test):
    logger.debug('Collecting Running Processes..')
    if test:
        return "test_processes"
    command = "ps aux"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting running processes",
                                  "Running processes collected")
    return ssh_command_out


def collect_scheduled_tasks(host_ssh_client,
                            test):
    logger.debug('Collecting Scheduled Tasks..')
    if test:
        return "test_scheduled_tasks"
    command = "cat /etc/crontab"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting scheduled tasks",
                                  "Scheduled tasks collected")
    return ssh_command_out


def collect_packages(host_ssh_client,
                     test):
    logger.debug('Collecting Installed Packages ..')
    if test:
        return "test_packages"
    command = "dpkg -l"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting installed packages",
                                  "Installed packages collected")
    return ssh_command_out


def collect_updates(host_ssh_client,
                    test):
    logger.debug('Collecting Updates..')
    if test:
        return "test_updates"
    command = "sudo apt-get update && apt list --upgradable"
    ssh_command_out = ssh_command(host_ssh_client,
                                  command,
                                  "Error while collecting available updates",
                                  "Available updates collected")
    return ssh_command_out
