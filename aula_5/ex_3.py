
class Contador:

    def __init__(self):
        self.conta = 0
        
    def contar(self):
        self.conta = self.conta + 1
        #abreviar a variarel : self.conta += 1

    # Codigo cliente
contador = Contador()
for i in range(10):
    contador.contar()
print(contador.conta)
