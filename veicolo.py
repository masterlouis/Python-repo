class veicolo:
    def __init__(self, marca, modello, anno, velocita):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocita = velocita
    def accelera(self):
        self.velocita += 10

class automobile(veicolo):
    def __init__(self, marca, modello, anno, velocita, porte):
        super().__init__(marca, modello, anno, velocita)
        self.porte = porte
    def stampa_informazioni(self):
        print("marca:", self.marca)
        print("modello: ", self.modello)
        print("anno: ", self.anno)
        print("velocita: ", self.velocita)
        print("Porte: ", self.porte)

auto1 = automobile("toyota", "hybrid", 2021, 120, 4)


print("Informazioni auto1")
auto1.stampa_informazioni()
auto1.accelera()
print("RISTAMPA")
auto1.stampa_informazioni()  #in queste ultime righe ho stampato i dati della machhina, ho fatto accelerare il veicolo e ho ristampato i dati