class File:
    def __init__(self,name,content):
        self.name = name
        self.mode = 'X' # Cerrado
        self.content = content
        self.size = len(content)
        self.pointer = 0

    def movePointer(self,bytes):
        if bytes > self.size :
            return -1
        self.pointer = bytes
        return 0
    
    def isOpen(self):
        return False if self.mode == 'X' else True


    def open(self,mode):
        if mode == 'R': 
            self.mode = 'R'      # Abierto en modo lectura
        elif mode == 'W': 
            self.content = ''
            self.pointer = 0
            self.mode = 'W'     # Abierto en modo escritura
        elif mode == 'A': 
            self.mode = 'A'     # Abierto en modo modificación
        else:
            return -1
        return 0

    def close(self):
        self.mode = 'X'
        self.pointer = 0

    def write(self,data):
        if self.mode == 'R':
            return -1
        leftSide = self.content[0:self.pointer]
        rightSide = self.content[self.pointer+len(data):self.size]
        self.content = leftSide+data+rightSide
        self.size = len(self.content)
        return 0
    
    def read(self,bytes):
        if not self.mode in ('R','A'):
            return -1
        return self.content[self.pointer:bytes+self.pointer]


    