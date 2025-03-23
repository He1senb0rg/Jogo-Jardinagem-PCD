from plantas.planta import Planta

class Batata(Planta):
    def __init__(self):
        super().__init__("Batata", 4)
        self.estado_crescimento = ["semente", "rebento", "madura", "pronto-recolher"]