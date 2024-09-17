# system-info-collector

## Collect system information from various hosts and create a csv file with all details

## Introduction

This project is a utility that ssh to a list of hosts and collects details about there status.

## Configuration

To configure this system to ssh to other hosts, you must define several environment variables in the `.env` file:

### Environment configuration

- `SSH_KEY_PATH`: Path to your private SSH key.
- `SSH_PORT`: SSH port number.
- `SSH_USER`: SSH username.
- `SSH_HOSTS`: A comma-separated list with hostnames or IP addresses.
- `COLLECT_HOSTNAME`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_UPTIME`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_DATE`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_OS`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_KERNEL`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_OS_DISK`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_IP`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_FIREWALL`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_PORTS`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_USERS`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_GROUPS`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_SERVICES`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_PROCESSES`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_SCHEDULED_TASKS`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_PACKAGES`: Set to `True` to collect. Otherwise, set to `False`.
- `COLLECT_UPDATES`: Set to `True` to collect. Otherwise, set to `False`.
- `REPORT_PATH`: The local host's path where the report will be stored.


## Getting Started

To properly set up the environment and collect system information from remote hosts, follow these steps:

1. Ensure that the host running the script can establish an SSH connection to all listed hosts.
2. Set up your SSH keys and make sure they are configured correctly on all remote hosts.
3. Set up the python environment by running the command "./bin/setup_venv" at the project root folder.
4.Set  up the cronjob by running the command "./bin/setup_cron" at the project root folder.

By doing so the deployment is ready and runs every three days at noon.

## Manual Run

To run the program manual you must complete steps 1-3 as described above. 

There are two options to run the program:

1. At the project root directory execute the command: './bin/collect_info.sh' to run the script that initiates the program.
2. At the project root directory execute the command: 'python3 main.py' to run directly the python code.

## Testing and Logs

The program offers a test option where there is no info collection from the remote hosts. It only tests ssh connectivity, file creation/permissions.

To initiate a test run at the project root directory execute the command: 'python3 main.py --test'.

Logs can be found at the project directory in the log folder. Log file collect_info.log is for the cron job and log file main.log comes from the python code itself.
