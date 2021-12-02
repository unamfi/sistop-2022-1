from os import kill, system as sys
from getpass import getuser as ge
import re

class File: 
    def __init__(self, name):
        self.name = name  #NOMBRE DEL ARCHIVO
        self.status = 0  # SI ESTA ABIERTO O NO {0: CERRADO, 1: ABIERTO}
        self.mode = '' #MODO 
        self.position = 0 #DESDE DONDE APUNTA EL ARCHIVO
        self.content = "" #CONTENIDO DEL ARCHIVO 
        self.size = 0 #TAMANO DEL ARCHVO

    def chstat(self) : self.status = ~self.status

    def chmode(self,mode): self.mode = self.__check_mode(mode)

    def __chsize(self): # REGRESA EL VALOR DE TAMANO VIRTUAL, COMPARANDO LA POSICION FRENTE AL CONTENIDO
        self.size = self.position if self.position >= len(self.content) else len(self.content)

    def __check_mode(self, mode): # CHECAR LOS MODOS VALIDOS EN LOS CUALES PODEMOS ABRIR UN ARCHVO
        valid_modes = ['R', 'W', 'A']
        if mode.upper() in valid_modes or mode == '': 
            return mode.upper()

        else:  
            print(f'Unvalid mode > mode given: {mode} only expected {valid_modes}')
            print('File will remain closed')
            return ''

    def able_to_read_write(self, mode, valid_modes):  #REGRESA SI UN ARCHIVO PUEDE LEER O ESCRIBIR UN ARCHIVO PASANDO LOS MODOS VALIDOS 
        return 1 if mode in valid_modes else 0

    def add_content(self,buffer): # INGRESAR CONTENIDO AL ARCHIVO CONSIDERANDO POSICIONES
        l = list(self.content)
        if self.position == 0 or self.position >= len(self.content): # SI POSICION ES 0 O SUPERA LA LONGITUD DEL CONTENIDO
            l[ len(self.content): ] = buffer  
       
        else: l[self.position-1 : len(buffer) + self.position-1] = buffer # SI NO SUPERA LA LONGITUD DEL CONTENIDO
        
        self.content = "".join(l)
        self.__chsize()  #LLAMADA AL AJUSTE DE TAMANO
        
    def chpost(self, position): 
        self.position = position
        self.__chsize() 


class Directory: 
    def __init__(self, name):
        self.name = name
        self.files = []

    def touch(self, file_name):
        self.files.append(File(file_name))

    def find_file(self,name):
        attemps = 0 # INTENTOS DE BUSQUEDA EN EL DIRECTORIO

        for f in self.files:
            if name == f.name: return f #REGRESAR EL ARCHIVO DE TIPO FILE
            else: attemps += 1
        if attemps == len(self.files) : return 'File not Found' # REGRESAR UN STRING


class Shell: 
    def __init__(self):
        self.dir = Directory('Master')
        self.__example_files()

    def __example_files(self):
        for i in ['hola','mis_tareas','pendientes']: self.dir.touch(i) 
    
    def ls(self): 
        for f in self.dir.files:
            print(f'Status:{f.status*-1} | Mode:{f.mode} | Size:[{f.size} bytes] \tName:{f.name}')   

    def open(self, name, mode): 
        f = self.dir.find_file(name)
        if type(f) == File: 
            if f.status == 0:
                f.chstat()  
                f.chmode(mode)
            else : 
                f.chmode(mode)
        else : print(f)

    def close(self, name): 
        f = self.dir.find_file(name) # EXISTE EL ARCHIVO?

        if type(f) == File : 
            if f.status == -1: # SI SE ENCUENTRA ABIERTO
                f.chstat()  #CERRAMOS EL ARCHIVO
                f.chmode('') #QUITAMOS LOS PERMISOS
            else : pass #SI YA ESTA CERRADO NO HAGAS NADA
        else : print(f)

    def write(self, name, len_buffer, buffer):
        f = self.dir.find_file(name) #EXISTE EL ARCHIVO?
        if type(f) == File: 
            if f.status: #SI ESTA ABIERTO 
                if f.able_to_read_write(f.mode,['W','A']): #SI TIENE LOS PERMISOS ADECUADOS
                    if len_buffer == len(buffer): #SI LA LONGITUD INGRESADA COINCIDE CON LA LONGITUD DEL CONTENIDO
                        f.add_content(buffer)   
                    else:
                        print('Cannot write, length value does not match with buffer length')
                else:
                    print(f'Write Permission denied \nFile mode {f.mode}') 
                    print(f'You must set file in mode W or A')
            else: 
                print('File is not open')
        else : 
            print(f)

    def read(self,name,bytes_to_read):
        f = self.dir.find_file(name) #SI EL ARCHIVO EXISTE?
        if type(f) == File:     
            if f.status:  #SI ESTA ABIERTO
                if f.able_to_read_write(f.mode,['R','A']): #SI ESTE TIENE LOS PERMISOS DE LECTURA
                    print(f.content[:bytes_to_read]) # IMPRIMIMOS EL MENSAJE
                else:
                    print(f'Read Permission denied \nFile mode {f.mode}') 
                    print(f'You must set file in mode R or A')
            else: 
                print('File is not open')
        else: print(f)

    def seek(self, name, position):
        f = self.dir.find_file(name) #EXISTE EL ARCHVO?
        
        if type(f) == File: 
            if f.status: # SI ESTA ABIERTO EL ARCHIVO?
                f.chpost(position)  #CAMBIO DE POSICION
            else: print('File is not open')
        else: print(f)

    def help(self):
        print(f'\ndir → Muestra el directorio')
        print(f'\nopen <arch> <modo> → Especifica que operaremos con el archivo de nombre "arch", empleando el modo especificado. Entrega un descriptor de archivo numérico.\n')
        print(f'\nclose <arch>   →    Termina una sesión de trabajo con el archivo referido por el descriptor indicado. Después de un close, cualquier intento por usar ese archivo entregará error.\n')
        print(f'\nread <arch> <longitud> → Lee la cantidad de bytes especificada\n')
        print(f'\nwrite <arch> <longitud> <datos» → Escribe la cantidad de bytes especificada, guardando los datos indicados como parámetro\n')
        print(f'\nseek <arch> <ubicacion> → Salta a la ubuicación especificada del archivo.\n')
        print(f'\nquit → Detiene la ejecucion de la simulación')

    def touch(self,name):
        self.dir.touch(name) #crear nuevo archivo pero cerrado y vacio
            

    def eval_instruction(self,instructions): 

        if instructions[0] == 'ls':
            self.ls()
            return 0                
        elif instructions[0] == 'close':
            self.close(instructions[1])
            return 0
        
        elif instructions[0] == 'open': 
            self.open(instructions[1],instructions[2])
            return 0
        elif instructions[0] == 'read': 
            self.read(instructions[1],int(instructions[2]))
            return 0
        elif instructions[0] == 'write': 
            self.write(instructions[1], int(instructions[2]), instructions[3])
            return 0
        elif instructions[0] == 'seek':
            self.seek(instructions[1], int(instructions[2]))
            return 0
        elif instructions[0] == 'clear': 
            sys('clear') 
            return 0
        
        elif instructions[0] == 'help': 
            self.help()
            return 0
            
        elif instructions[0] == 'touch': 
            self.touch(instructions[1])
            return 0

        elif instructions[0] == 'quit': 
            return 1

        else: print(f'{instructions[0]} does not exist. Check sintax and try again')
    
    def console_input(self):
        
        while True: 
            try:
                instructions = re.split('\s|(?<!\d)[,.](?!\d)',(input(f'\n{username}:/{self.dir.name} ▶ '))) 
                e = self.eval_instruction(instructions)
                if e == 1:
                    break 
            
            except ValueError: print(f'Missing parameters for {instructions[0]}')
            
            except IndexError: print(f'Missing parameters for {instructions[0]}')

            #except: print('Something else went wrong : ☹')


if __name__ == "__main__":
    
    sys('clear')
    username = ge()
    s = Shell()
    s.console_input()
    