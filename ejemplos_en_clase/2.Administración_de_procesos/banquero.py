#!/usr/bin/python3
#
# Implementación ejemplo del algoritmo del banquero limitado a UNA CATEGORÍA
#
# (normalmente tendríamos una instancia de esto para cada una de las categorías de recursos)

# Serie de procesos
# Cada uno de los cuales: Necesidad máxima (reclamo), Asignado, Solicitado

class Proceso:
    def __init__(self, nombre, maximo):
        self.nombre = nombre
        self.maximo = maximo
        self.asignado = 0
        self.solicitado = 0

    def __str__(self):
        return '%s (Max:%d, Asig:%d, Solic:%d' % (self.nombre, self.maximo, self.asignado, self.solicitado)

    def por_pedir(self):
        return self.maximo - self.asignado

class Sistema:
    def __init__(self, total):
        self.total = total
        self.asignados = 0
        self.procesos = []

    def nuevo_proceso(self, proc):
        if proc.maximo <= self.total:
            self.procesos.append(proc)
            return True
        print('No puedo admitir al proceso solicitado')
        return False

    def libres(self):
        return self.total - self.asignados

    def solicita(self, proceso, num_rec):
        if proceso not in self.procesos:
            print('Proceso inválido')
            return False

        tot_procesos = self.procesos[:]
        secuencia = []
        libres_local = self.libres()
        while len(tot_procesos) > 0:
            p = list(filter(lambda x: x.por_pedir() < libres_local, tot_procesos))
            if len(p) == 0:
                print('Se solicitó un estado inseguro ☹')
                return False
            sig_proc = p[0]
            libres_local += sig_proc.asignado
            tot_procesos.remove(sig_proc)
            secuencia.append(sig_proc)

        self.asignados += num_rec
        print('La secuencia segura para otorgar %d a %s es:' % (num_rec, proceso))
        print(secuencia)
        print('y me quedo con %d disponibles.' % self.libres())

sist = Sistema(10)
p1 = Proceso('Uno', 5)
p2 = Proceso('Dos', 5)
p3 = Proceso('Tres', 3)
p4 = Proceso('Cuatro', 7)
sist.nuevo_proceso(p1)
sist.nuevo_proceso(p2)
sist.nuevo_proceso(p3)
sist.nuevo_proceso(p4)
print('La lista de procesos aceptados es:')
print(sist.procesos)

sist.solicita(p1, 2)
sist.solicita(p2, 3)
sist.solicita(p3, 2)
sist.solicita(p4, 4)
sist.solicita(p2, 1)
sist.solicita(p2, 1)

