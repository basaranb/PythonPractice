class MyClass():
    def _init_(self):
        self.s=""
    def getString(self):
        self.s=raw_input()
    def printString(self):
        print(self.s)

a=MyClass()
a.getString()
a.printString()
