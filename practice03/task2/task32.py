from struct import unpack

class C32:
    state = ''
    def __init__(self):
        self.state = 'A'
    def move(self):
        #если состояние A, B или C
        if self.state == 'A' or self.state == 'B':
            self.state = chr(ord(self.state) + 1)
            return ord(self.state) - 66
        elif self.state == 'C':
            self.state = 'D'
            return 3
        #если состояние F
        elif self.state == 'F':
            self.state = 'A'
            return 8
        else:
            raise RuntimeError
    
    def pluck(self):
        if self.state == 'C':
            self.state = 'F'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            return 7
        else:
            raise RuntimeError
    
    def sway(self):
        if self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'B':
            self.state = 'F'
            return 2
        else:
            raise RuntimeError

o = C32()
#o.sway()
print(o.move())
print(o.sway())
print(o.move())
print(o.move())
print(o.move())
print(o.move())
print(o.pluck())
print(o.pluck())
#print(o.move())
print(o.sway())
print(o.move())
print(o.move())
