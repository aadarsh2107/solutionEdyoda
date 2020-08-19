class stack1:
    def __init__(self):
        self.a=[]
        self.length=0
        self.maxvalue=[float("-inf")]
    def pop(self):
        if self.a[-1]==self.maxvalue[-1]:
            self.maxvalue.pop()
        del self.a[-1]
        self.length=self.length-1   
    def push(self,value):
        self.a.append(value)
        self.length=self.length+1 
        if self.maxvalue[-1]<=value:
            self.maxvalue.append(value)
    def printstack(self):
        print(self.a)
    def max(self):
        if self.maxvalue[-1]!=float("-inf"):
            print(self.maxvalue[-1])
a=stack1()       
a.push(2)
a.push(1)
a.push(8)
a.push(7)
a.push(7)
a.max()
a.pop()
a.max()
a.pop()
a.max()
a.pop()
a.max()
a.printstack()
