#!/usr/bin/env python
#-*-coding:utf8-*-
# Author: wang.chenhao@sfit.shfe.com.cn


import paramiko
import getpass
import sys


def ssh2(host, username, password, cmds, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port, username, password, timeout=5)
    except (paramiko.ssh_exception.AuthenticationException):
        print 'Login failed by Username: \033[1;30m{}\033[0m, Password: \033[1;30m{}\033[0m.'.format(username, password)
        sys.exit(1)
    except (paramiko.ssh_exception.NoValidConnectionsError):
        print 'Unable to connect to port \033[1;30m{}\033[0m on \033[1;30m{}\033[0m.'.format(port, host)
        sys.exit(2)

    for cmd in cmds:
        print '\n\033[1;30mHost: %s, Task: %s\033[0m.'.format(host, cmd)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        for line in stdout:
            print line,

        while True:
            try:
                result = raw_input('Continue? (y/n): ')
            except (KeyboardInterrupt, EOFError):
                print
                sys.exit(0)
            if result == 'y' or result == 'Y':
                break

    ssh.close()


def menu():
    prompt = '''(1) 第一部分
(2) 第二部分
请选择需要检测的内容(1/2):  '''
    while True:
        try:
            index = raw_input(prompt).strip()[0]
        except (KeyboardInterrupt, EOFError):
            print
            sys.exit(0)
        except (IndexError):
            continue
        if index == '1' or index == '2':
            break

    return index


if __name__ == '__main__':
    try:
        username = raw_input('Username: ')
        password = getpass.getpass('Password: ')
    except (KeyboardInterrupt, EOFError):
        print
        sys.exit(0)

    l = ['show inter status', 'show logging', 'show ip ospf neighbor', 'show standby brief', 'show proc cpu his',\
         'show fabric channel-counters', 'show etherchannel summary', 'show redundancy', 'show environment status',\
         'show ip int brief', 'show platform', 'show environment all', 'show environment status', 'show hsrp brief',\
         'show port-channel summary', 'show redundancy status', 'show environment']

    choice = menu()
    if choice == '1':
        # 网络连通性(第一部分)
        ssh2('ZJ-TY1004-A1-2NAGG', username, password, \
             ['ping 10.64.0.17 -c 3', 'ping 10.64.0.29 -c 3', 'ping 10.208.4.2 -c 3'])
        ssh2('ZJ-TY1004-A2-2NAGH', username, password, \
             ['ping 10.64.0.21 -c 3', 'ping 10.64.0.25 -c 3', 'ping 10.208.16.2 -c 3'])
        ssh2('ZJ-TY1004-A3-2NAGG', username, password, \
             ['ping 10.32.0.17 -c 3', 'ping 10.32.0.29 -c 3', 'ping 10.112.22.2 -c 3'])
        ssh2('ZJ-TY1004-A4-2NAGH', username, password, \
             ['ping 10.32.0.21 -c 3', 'ping 10.32.0.25 -c 3', 'ping 10.112.22.6 -c 3'])
        ssh2('Z.11-S2.1-R1002X-A1-2NAHE', username, password, ['ping 10.14.250.249 -c 3'])
        ssh2('Z.11-S2.1-R1002X-A2-2NAHE', username, password, ['ping 10.14.249.249 -c 3'])
        ssh2('Z.11-S2.1-R1002X-A3-2NAHF', username, password, ['ping 10.94.250.249 -c 3'])
        ssh2('Z.11-S2.1-R1002X-A4-2NAHF', username, password, ['ping 10.94.249.249 -c 3'])
        ssh2('Z.11-HL1-S3750X-2NAHC', username, password, l[:1])
        ssh2('J.2-HL1-S3750X-E506', username, password, l[:1])
        ssh2('Z.11-HL2-S3750G-2NAHC', username, password, l[:1])

        # 特别设备专项检查(第一部分)
        ssh2('Z.11-A2-R7606-C1-2NAGG', username, password, l[1:9] + \
             ['ping 172.16.224.161 -c 3', 'ping 172.16.228.121 -c 3', 'ping 172.16.241.1 -c 3'])
        ssh2('Z.11-A2-R7606-C2-2NAGG', username, password, l[1:9] + \
             ['ping 172.16.224.161 -c 3', 'ping 172.16.228.121 -c 3', 'ping 172.16.241.1 -c 3'])
        ssh2('Z.11-A2-R1004-A1-2NAGG', username, password, l[1:3] + l[4:5] + l[7:8] + l[9:12])
        ssh2('Z.11-A2-R1004-A2-2NAGH', username, password, l[1:3] + l[4:5] + l[7:8] + l[9:12])
        ssh2('Z.11-A2-R1004-A3-2NAGG', username, password, l[1:3] + l[4:5] + l[7:8] + l[9:12])
        ssh2('Z.11-A2-R1004-A4-2NAGH', username, password, l[1:3] + l[4:5] + l[7:8] + l[9:12])
        ssh2('Z.11-S2-S6506-D1-2NAGE', username, password, l[:2] + l[3:9])
        ssh2('Z.11-S2-S6506-D2-2NAGF', username, password, l[:2] + l[3:9])
        ssh2('Z.12-S2-S6506-D1-2NAAC', username, password, l[:2] + l[3:9])
        ssh2('Z.12-S2-S6506-D2-2NAAD', username, password, l[:2] + l[3:9])
        ssh2('Z.3-S2-S7009-D1-1M811', username, password, l[:3] + l[4:5] + l[-4:])
        ssh2('Z.3-S2-S7009-D2-1M812', username, password, l[:3] + l[4:5] + l[-4:])
        ssh2('Z.3-S1-S7009-D1-1M809', username, password, l[:3] + l[4:5] + l[-4:] + \
             ['ping 172.16.243.1 -c 3', 'ping 172.16.243.22 -c 3'])
        ssh2('Z.3-S1-S7009-D2-1M810', username, password, l[:3] + l[4:5] + l[-4:] + \
             ['ping 172.16.243.1 -c 3', 'ping 172.16.243.22 -c 3'])
        ssh2('Z.11-A3-S7009-C1-2NAHA', username, password, l[:3] + l[4:5] + l[-4:] + \
             ['ping 172.16.243.9 -c 3'])
        ssh2('Z.11-A3-S7009-C2-2NAHB', username, password, l[:3] + l[4:5] + l[-4:] + \
             ['ping 172.16.243.9 -c 3'])
        ssh2('Z.11-A31-R1004-A1-2NAHA', username, password, l[1:3] + l[4:5] + l[9:10] + l[-1:] + \
             ['ping 10.253.0.1 -c 3'])
        ssh2('Z.11-A31-R1004-A2-2NAHB', username, password, l[1:3] + l[4:5] + l[9:10] + l[-1:] + \
             ['ping 10.253.8.1 -c 3'])

    else:
        pass



