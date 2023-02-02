class persona:
    def __init__(self, a, b):
        self.nome = a
        self.eta = b
    
    def presentazione(self):
        print("ciao, mi chiamo", self.nome, "e ho", self.eta, "anni")

giulio = persona("giulio", 35)

giulio.presentazione()