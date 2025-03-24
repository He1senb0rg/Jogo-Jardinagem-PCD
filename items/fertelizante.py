from items.item import Item

class Fertelizante(Item): #faz com q a planta cresça mais rápido
    def __init__(self):
        super().__init__("Fertelizante", 5)
        self.eficacia = 2

    def aplicar(self, planta):
        planta.eficacia_crescimento = self.eficacia
        print(f"Fertelizaste a {planta.nome} com {self.eficacia}x de eficácia")