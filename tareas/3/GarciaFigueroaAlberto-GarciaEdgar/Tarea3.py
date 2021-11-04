def main():
    repite=True
    while(repite):
        print("Bienvenido, seleccione el algoritmo que desee que se analice")
        print("1.- Algoritmo FCFS")
        print("2.- Algoritmo RR")
        print("3.- Algoritmo SPN")
        print("4.- Algoritmo SRR")
        print("5.- Salir del programa")
        a=int(input("-->"))
        if (a==1):
            print("Se hace FCFS")
        elif (a==2):
            print("Se hace RR")
        elif (a==3):
            print("Se hace SPN")
        elif (a==4):
            print("Se hace SRR")
        elif (a==5):
            repite=False
        else:
            print("Vuelva a introducir un valor")
            a=int(input("-->"))
        
main()
