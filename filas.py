class Fila():
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)
        
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        pass
class Fila():
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)
        
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):

        return not len(self.data) > 0