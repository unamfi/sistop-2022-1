class Process:
    def __init__(self, id, arrvl_time, exec_time):
        self.id = id
        self.arrvl_time = arrvl_time
        self.exec_time = exec_time
        self.compl_time = 0
        self.timeLeft = exec_time

    def execute(self, quantum):
        #self.timeLeft = self.timeLeft - quantum if self.timeLeft > quantum else 0
        if self.timeLeft > quantum:
            self.timeLeft = self.timeLeft - quantum
            return False
        else:
            self.timeLeft = 0
            return True

