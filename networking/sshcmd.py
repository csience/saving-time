#!/usr/bin/env python2

import threading
import paramiko
import subprocess

# can setup to run multiple commands on SSH server or run commands on multiple SSH servers
def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    # client.load_host_keys('~/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print
        ssh_session.recv(1024)
    return

def main():
    ip = raw_input('IP Address:')
    user = raw_input('Username:')
    passwd = raw_input('Password:')
    command = raw_input('Command:')

    # ssh_command('192.168.1.122', 'michael', 'password@!@#', 'id')
    ssh_command(ip, user, passwd, command)

if __name__ == "__main__":
    main()
