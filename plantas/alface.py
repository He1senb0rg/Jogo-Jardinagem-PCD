from plantas.planta import Planta

class Alface(Planta):
    def __init__(self):
        super().__init__("Alface", 5)
        self.estado_crescimento = ["semente", "rebento", "madura", "pronto-recolher"]