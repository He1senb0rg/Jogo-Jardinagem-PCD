from plantas.planta import Planta

class Cenoura(Planta):
    def __init__(self):
        super().__init__("Cenoura", 8)
        self.estado_crescimento = ["semente", "rebento", "madura", "pronto-recolher"]