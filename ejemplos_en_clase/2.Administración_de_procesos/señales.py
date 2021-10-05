#!/usr/bin/python3
from time import sleep
import signal, os

mi_pid = os.getpid()
print('Iniciando este programa sencillito. Mi PID es %d' % mi_pid)

def muere_limpio(sig,frame):
    print("Me dijeron que me vaya (señal %d). Yo me voy." % sig)
    exit(1)

def no_te_mueras(sig,frame):
    print('Qué... ¿Crees que puedes conmigo? ¿Con una simple señal %d? ¡Muajajajaja!' % sig)

def terminal(sig,frame):
    print('Esta terminal mide:')
    print(os.get_terminal_size())

# SIGINT es la señal #2
# SIGTERM es #15
# SIGKILL es #9
signal.signal(signal.SIGINT, no_te_mueras)
signal.signal(signal.SIGTERM, no_te_mueras)
# signal.signal(signal.SIGKILL, no_te_mueras)

signal.signal(signal.SIGWINCH, terminal)

while True:
    sleep(2)
