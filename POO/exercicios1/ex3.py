class ClasseA():
    def __init__(self):
        pass
    
    def mostrar(self):
        print("A")
        
class ClasseB():
    def __init__(self):
        pass
    
    def mostrar(self):
        print("B")

class ClasseC(ClasseB, ClasseA):
    pass

objetoC = ClasseC()
objetoC.mostrar()
print(ClasseC.__mro__)

# Nota: Python sempre segue da esquerda → pra direita (MRO)
# Jeito de ver: print(C.__mro__)