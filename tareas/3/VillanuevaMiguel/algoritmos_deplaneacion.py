import random
import copy

def fifo(procesos_datos):
    T=0
    T1=0
    t_inicial=0
    E=0
    P=0
    resultado=[]
    
    for i in range(len(procesos_datos)):
        t_llegada=procesos_datos[i][1]
        t_n=procesos_datos[i][2]
        T1=((t_inicial - t_llegada)+t_n)
        T=T+T1
        #print('T1=',T1)
        E1=T1-t_n
        #print('E1=',E1)
        P1=T1/t_n
        #print('P1=',P1)
        E=E+E1
        P=P+P1
        t_inicial=t_inicial + t_n
        Ttotal=T/len(procesos_datos)
        Etotal=E/len(procesos_datos)
        Ptotal=P/len(procesos_datos)
        letra=procesos_datos[i][0]
        if t_n > 0:
            letra=letra*t_n
            resultado.append(letra)
    print("".join(resultado))
    print("FIFO: T=",Ttotal," E=",Etotal,"P=",Ptotal)
    

def rr1(procesos_datos):
    proc_final=[]
    cadena=''
    datos=copy.deepcopy(procesos_datos)
    E=0
    T=0
    P=0
    cont=0
    condicion=len(datos)
    while condicion>0:
        for i in range(len(procesos_datos)):
            t_llegada1=datos[i][1]
            t_n1=datos[i][2]
            letra1=datos[i][0]
            if t_llegada1 <= cont and t_n1>0:
                cadena += letra1
                t_n1 -= 1
                datos[i][2]=t_n1
                cont+=1   
            if t_n1==0 and letra1 not in proc_final:
                t_llegada=procesos_datos[i][1]
                t_n=procesos_datos[i][2]
                T1=len(cadena)-t_llegada
                #print(T1)
                T=T1+T
                E1=T1-t_n
                E=E1+E
                P1=T1/t_n
                P=P+P1
                Ttotal=T/len(procesos_datos)
                Etotal=E/len(procesos_datos)
                Ptotal=P/len(procesos_datos)
                proc_final.append(letra1)
                condicion-=1
    print(cadena)
    print("RR1: T=",Ttotal,"  E=",Etotal,"  P=",Ptotal)
            
def spn(procesos_datos):
    espera=[]
    proc_final=[]
    datos=copy.deepcopy(procesos_datos)
    cadena=''
    cadena1=''
    E=0
    T=0
    P=0
    cont=0
    i=0
    while i < len(datos):
        t_llegada1=datos[i][1]
        t_n1=datos[i][2]
        letra1=datos[i][0]
        if t_llegada1 == cont:
            cadena1= letra1*t_n1
            cont += t_n1
            t_n1 = 0
            datos[i][2]=t_n1   
            cadena+=cadena1
            i+=1
        elif i ==len(datos)-1:
            cadena1= letra1*t_n1
            cont+= t_n1
            t_n1 = 0
            datos[i][2]=t_n1
            i+=1
            cadena+=cadena1
        elif t_n1<=datos[i+1][2]:
            cadena1= letra1*t_n1
            cont+= t_n1
            t_n1 = 0
            datos[i][2]=t_n1  
            i+=1
            cadena+=cadena1
        elif t_n1>datos[i+1][2]:
            cadena1= datos[i+1][0]*datos[i+1][2]
            cont+= datos[i+1][2]
            datos[i+1][2] = 0 
            cadena+=cadena1
            D1=datos[i+1][0]
            D2=datos[i+1][1]
            D3=datos[i+1][2]
            datos[i+1][0]=letra1
            datos[i+1][1]=t_llegada1
            datos[i+1][2]=t_n1
            i+=1

        if t_n1 == 0 and letra1 not in proc_final:
            t_llegada=procesos_datos[i-1][1]
            t_n=procesos_datos[i-1][2]
            T1=len(cadena)-t_llegada
            #print(T1)
            T=T1+T
            E1=T1-t_n
            #print("e1=",E1)
            E=E1+E
            P1=T1/t_n
            #print("p1=",P1)
            P=P+P1
            Ttotal=T/len(procesos_datos)
            Etotal=E/len(procesos_datos)
            Ptotal=P/len(procesos_datos)
            proc_final.append(letra1)

        elif D3 == 0 and D1 not in proc_final:
            t_llegada=procesos_datos[i][1]
            t_n=procesos_datos[i][2]
            T1=len(cadena)-t_llegada
            #print(T1)
            T=T1+T
            E1=T1-t_n
            #print("e1=",E1)
            E=E1+E
            P1=T1/t_n
            #print("p1=",P1)
            P=P+P1
            Ttotal=T/len(procesos_datos)
            Etotal=E/len(procesos_datos)
            Ptotal=P/len(procesos_datos)
            proc_final.append(datos[i][2])
            

    print(cadena)
    print("SPN: T=",Ttotal,"  E=",Etotal,"  P=",Ptotal)

proceso=["A","B","C","D","E"]
procesos_datos=[]
proceso_llegada=0

#procesos_datos=[['A',0, 3], ['B', 1,5],['C',3,2],['D', 9, 5], ['E', 12, 5]]

for i in range(len(proceso)):
    proceso_t=random.randint(1,10)
    procesos_datos.append([proceso[i],proceso_llegada,proceso_t])
    proceso_llegada += random.randint(1,5)
    
print(procesos_datos)
fifo(procesos_datos)
rr1(procesos_datos)
spn(procesos_datos)