#1/usr/bin/python3
import os

pid = os.fork()

if pid > 0:
    os.wait()
    print('El hijo (%d) terminó.' % pid)
else:
    os.execve('/usr/bin/ls', ['ls', '-l'], {'LANG': 'en_US.UTF-8'})

