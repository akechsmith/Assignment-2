class Calculator:

    def __init__(self, a, b): 
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
    def mod(self):
        return self.a % self.b

calc1 = Calculator(10, 5)
print(calc1.add())
print(calc1.sub())
print(calc1.mul())
print(calc1.div())
print(calc1.mod())