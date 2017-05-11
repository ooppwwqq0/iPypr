#!/usr/bin/env python
# -*- coding: utf-8 -*-

from iPypr import pypr
import json

def main():
    data = [{u'shell': True, u'workphone': [], u'uid': '', u'passwd': u'x', u'roomnumber': u'', u'gid': 0, u'groups': [u'root'], u'home': u'/root', u'fullname': u'root', u'homephone': u'', u'name': u'root'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 1, u'passwd': u'x', u'roomnumber': u'', u'gid': 1, u'groups': [u'bin', u'daemon', u'sys'], u'home': u'/bin', u'fullname': u'bin', u'homephone': u'', u'name': u'bin'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 2, u'passwd': u'x', u'roomnumber': u'', u'gid': 2, u'groups': [u'adm', u'bin', u'daemon', u'lp'], u'home': u'/sbin', u'fullname': u'daemon', u'homephone': u'', u'name': u'daemon'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 3, u'passwd': u'x', u'roomnumber': u'', u'gid': 4, u'groups': [u'adm', u'sys'], u'home': u'/var/adm', u'fullname': u'adm', u'homephone': u'', u'name': u'adm'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 4, u'passwd': u'x', u'roomnumber': u'', u'gid': 7, u'groups': [u'lp'], u'home': u'/var/spool/lpd', u'fullname': u'lp', u'homephone': u'', u'name': u'lp'}, {u'shell': u'/bin/sync', u'workphone': u'', u'uid': 5, u'passwd': u'x', u'roomnumber': u'', u'gid': 0, u'groups': [u'root'], u'home': u'/sbin', u'fullname': u'sync', u'homephone': u'', u'name': u'sync'}, {u'shell': u'/sbin/shutdown', u'workphone': u'', u'uid': 6, u'passwd': u'x', u'roomnumber': u'', u'gid': 0, u'groups': [u'root'], u'home': u'/sbin', u'fullname': u'shutdown', u'homephone': u'', u'name': u'shutdown'}, {u'shell': u'/sbin/halt', u'workphone': u'', u'uid': 7, u'passwd': u'x', u'roomnumber': u'', u'gid': 0, u'groups': [u'root'], u'home': u'/sbin', u'fullname': u'halt', u'homephone': u'', u'name': u'halt'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 8, u'passwd': u'x', u'roomnumber': u'', u'gid': 12, u'groups': [u'mail'], u'home': u'/var/spool/mail', u'fullname': u'mail', u'homephone': u'', u'name': u'mail'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 10, u'passwd': u'x', u'roomnumber': u'', u'gid': 14, u'groups': [u'uucp'], u'home': u'/var/spool/uucp', u'fullname': u'uucp', u'homephone': u'', u'name': u'uucp'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 11, u'passwd': u'x', u'roomnumber': u'', u'gid': 0, u'groups': [u'root'], u'home': u'/root', u'fullname': u'operator', u'homephone': u'', u'name': u'operator'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 12, u'passwd': u'x', u'roomnumber': u'', u'gid': 100, u'groups': [u'users'], u'home': u'/usr/games', u'fullname': u'games', u'homephone': u'', u'name': u'games'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 13, u'passwd': u'x', u'roomnumber': u'', u'gid': 30, u'groups': [u'gopher'], u'home': u'/var/gopher', u'fullname': u'gopher', u'homephone': u'', u'name': u'gopher'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 14, u'passwd': u'x', u'roomnumber': u'', u'gid': 50, u'groups': [u'ftp'], u'home': u'/var/ftp', u'fullname': u'FTP User', u'homephone': u'', u'name': u'ftp'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 99, u'passwd': u'x', u'roomnumber': u'', u'gid': 99, u'groups': [u'nobody'], u'home': u'/', u'fullname': u'Nobody', u'homephone': u'', u'name': u'nobody'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 69, u'passwd': u'x', u'roomnumber': u'', u'gid': 69, u'groups': [u'vcsa'], u'home': u'/dev', u'fullname': u'virtual console memory owner', u'homephone': u'', u'name': u'vcsa'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 173, u'passwd': u'x', u'roomnumber': u'', u'gid': 173, u'groups': [u'abrt'], u'home': u'/etc/abrt', u'fullname': u'', u'homephone': u'', u'name': u'abrt'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 38, u'passwd': u'x', u'roomnumber': u'', u'gid': 38, u'groups': [u'ntp'], u'home': u'/etc/ntp', u'fullname': u'', u'homephone': u'', u'name': u'ntp'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 499, u'passwd': u'x', u'roomnumber': u'', u'gid': 76, u'groups': [u'saslauth'], u'home': u'/var/empty/saslauth', u'fullname': u'Saslauthd user', u'homephone': u'', u'name': u'saslauth'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 89, u'passwd': u'x', u'roomnumber': u'', u'gid': 89, u'groups': [u'mail', u'postfix'], u'home': u'/var/spool/postfix', u'fullname': u'', u'homephone': u'', u'name': u'postfix'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 74, u'passwd': u'x', u'roomnumber': u'', u'gid': 74, u'groups': [u'sshd'], u'home': u'/var/empty/sshd', u'fullname': u'Privilege-separated SSH', u'homephone': u'', u'name': u'sshd'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 72, u'passwd': u'x', u'roomnumber': u'', u'gid': 72, u'groups': [u'tcpdump'], u'home': u'/', u'fullname': u'', u'homephone': u'', u'name': u'tcpdump'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 81, u'passwd': u'x', u'roomnumber': u'', u'gid': 81, u'groups': [u'dbus'], u'home': u'/', u'fullname': u'System message bus', u'homephone': u'', u'name': u'dbus'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 28, u'passwd': u'x', u'roomnumber': u'', u'gid': 28, u'groups': [u'nscd'], u'home': u'/', u'fullname': u'NSCD Daemon', u'homephone': u'', u'name': u'nscd'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2001, u'passwd': u'x', u'roomnumber': u'', u'gid': 2001, u'groups': [u'nanu', u'wheel'], u'home': u'/home/nanu', u'fullname': u'', u'homephone': u'', u'name': u'nanu'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2002, u'passwd': u'x', u'roomnumber': u'', u'gid': 2002, u'groups': [u'haibo', u'wheel'], u'home': u'/home/haibo', u'fullname': u'', u'homephone': u'', u'name': u'haibo'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2003, u'passwd': u'x', u'roomnumber': u'', u'gid': 2003, u'groups': [u'minzaohua', u'wheel'], u'home': u'/home/minzaohua', u'fullname': u'', u'homephone': u'', u'name': u'minzaohua'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 1001, u'passwd': u'x', u'roomnumber': u'', u'gid': 1001, u'groups': [u'www'], u'home': u'/home/www', u'fullname': u'', u'homephone': u'', u'name': u'www'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 1002, u'passwd': u'x', u'roomnumber': u'', u'gid': 1002, u'groups': [u'mysql'], u'home': u'/home/mysql', u'fullname': u'', u'homephone': u'', u'name': u'mysql'}, {u'shell': u'/sbin/nologin', u'workphone': u'', u'uid': 1003, u'passwd': u'x', u'roomnumber': u'', u'gid': 1003, u'groups': [u'redis'], u'home': u'/data/redis', u'fullname': u'', u'homephone': u'', u'name': u'redis'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2004, u'passwd': u'x', u'roomnumber': u'', u'gid': 2004, u'groups': [u'wangchao', u'wheel'], u'home': u'/home/wangchao', u'fullname': u'', u'homephone': u'', u'name': u'wangchao'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2005, u'passwd': u'x', u'roomnumber': u'', u'gid': 2005, u'groups': [u'wheel', u'xiongdecai'], u'home': u'/home/xiongdecai', u'fullname': u'', u'homephone': u'', u'name': u'xiongdecai'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2006, u'passwd': u'x', u'roomnumber': u'', u'gid': 2006, u'groups': [u'ophelp', u'wheel'], u'home': u'/home/ophelp', u'fullname': u'', u'homephone': u'', u'name': u'ophelp'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2007, u'passwd': u'x', u'roomnumber': u'', u'gid': 2007, u'groups': [u'wanglanbiao', u'wheel'], u'home': u'/home/wanglanbiao', u'fullname': u'', u'homephone': u'', u'name': u'wanglanbiao'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 1006, u'passwd': u'x', u'roomnumber': u'', u'gid': 1006, u'groups': [u'zabbix'], u'home': u'/home/zabbix', u'fullname': u'', u'homephone': u'', u'name': u'zabbix'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2008, u'passwd': u'x', u'roomnumber': u'', u'gid': 2008, u'groups': [u'rwuser'], u'home': u'/home/rwuser', u'fullname': u'', u'homephone': u'', u'name': u'rwuser'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2010, u'passwd': u'x', u'roomnumber': u'', u'gid': 2010, u'groups': [u'wheel', u'xuejichao'], u'home': u'/home/xuejichao', u'fullname': u'', u'homephone': u'', u'name': u'xuejichao'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2011, u'passwd': u'x', u'roomnumber': u'', u'gid': 2011, u'groups': [u'liyuanping', u'wheel'], u'home': u'/home/liyuanping', u'fullname': u'', u'homephone': u'', u'name': u'liyuanping'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2014, u'passwd': u'x', u'roomnumber': u'', u'gid': 2014, u'groups': [u'weizhenhua', u'wheel'], u'home': u'/home/weizhenhua', u'fullname': u'', u'homephone': u'', u'name': u'weizhenhua'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2015, u'passwd': u'x', u'roomnumber': u'', u'gid': 2015, u'groups': [u'wangping', u'wheel'], u'home': u'/home/wangping', u'fullname': u'', u'homephone': u'', u'name': u'wangping'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2016, u'passwd': u'x', u'roomnumber': u'', u'gid': 2016, u'groups': [u'wanghongwei', u'wheel'], u'home': u'/home/wanghongwei', u'fullname': u'', u'homephone': u'', u'name': u'wanghongwei'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2017, u'passwd': u'x', u'roomnumber': u'', u'gid': 2017, u'groups': [u'wheel', u'zhaoyuntao'], u'home': u'/home/zhaoyuntao', u'fullname': u'', u'homephone': u'', u'name': u'zhaoyuntao'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2018, u'passwd': u'x', u'roomnumber': u'', u'gid': 2018, u'groups': [u'wheel', u'wuzhuqu'], u'home': u'/home/wuzhuqu', u'fullname': u'', u'homephone': u'', u'name': u'wuzhuqu'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2019, u'passwd': u'x', u'roomnumber': u'', u'gid': 2019, u'groups': [u'salt'], u'home': u'/home/salt', u'fullname': u'', u'homephone': u'', u'name': u'salt'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2020, u'passwd': u'x', u'roomnumber': u'', u'gid': 2020, u'groups': [u'chenqiu', u'wheel'], u'home': u'/home/chenqiu', u'fullname': u'', u'homephone': u'', u'name': u'chenqiu'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2021, u'passwd': u'x', u'roomnumber': u'', u'gid': 2021, u'groups': [u'dingpeng', u'wheel'], u'home': u'/home/dingpeng', u'fullname': u'', u'homephone': u'', u'name': u'dingpeng'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2022, u'passwd': u'x', u'roomnumber': u'', u'gid': 2022, u'groups': [u'lizhengqi', u'wheel'], u'home': u'/home/lizhengqi', u'fullname': u'', u'homephone': u'', u'name': u'lizhengqi'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2023, u'passwd': u'x', u'roomnumber': u'', u'gid': 2023, u'groups': [u'jumproot'], u'home': u'/home/jumproot', u'fullname': u'', u'homephone': u'', u'name': u'jumproot'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2024, u'passwd': u'x', u'roomnumber': u'', u'gid': 2024, u'groups': [u'read'], u'home': u'/home/read', u'fullname': u'', u'homephone': u'', u'name': u'read'}, {u'shell': u'/bin/bash', u'workphone': u'', u'uid': 2025, u'passwd': u'x', u'roomnumber': u'', u'gid': 2025, u'groups': [u'deploy'], u'home': u'/home/deploy', u'fullname': u'', u'homephone': u'', u'name': u'deploy'},(1,2,3,45,6,"asdads","asdasd",[1,2,4,6,"asd"])]
    #print(json.dumps(data))
    pypr(data)
if __name__ == "__main__":
    main()

