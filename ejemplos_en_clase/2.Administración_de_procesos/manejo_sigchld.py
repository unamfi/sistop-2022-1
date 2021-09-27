#!/usr/bin/python3

import os
import signal
from time import sleep

pid_orig = os.getpid()
pid = os.fork()

def espera_al_hijo(sig, frame):
    print('El padre se da por enterado de que el hijo (%d) ya se fue' % pid)
    os.wait()

signal.signal(signal.SIGCHLD, espera_al_hijo)

if (pid > 0):
    print('Proceso padre. Sigo siendo %d, el hijo es %d' % (os.getpid(), pid))
    sleep(120)
else:
    print('Proceso hijo. Mi PID es %d. El fork me dio %d' % (os.getpid(), pid))
    sleep(3)
    print('El hijo ya se va.')
    exit(0)
