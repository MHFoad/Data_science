class Prepend (object):
    def __init__(self, s):
        self.start=s
    def write(self,s):
        print(self.start+ s)

p = Prepend("+++ ")
p.write("Hello")