import random
from .helper import Helper
from plantas.alface import Alface
from plantas.cenoura import Cenoura
from plantas.tomate import Tomate
from plantas.batata import Batata

class Jardineiro:
    """Representa um jardineiro que pode plantar, regar e recolher plantas."""

    def __init__(self, nome):
        self.nome = nome
        self.plantas_plantadas = []
        self.inventario = {}
        self.plantas_disponiveis = {"tomate": Tomate, "alface": Alface, "cenoura": Cenoura, "batata": Batata}
        self.rendimento = 0

    def plantar(self):
        if self.inventario == {}:
            print("Não tens plantas para plantar")
        else:
            planta_selecionada = Helper().seleccionar_item(self.inventario)
            if self.inventario[planta_selecionada] > 0:
                self.inventario[planta_selecionada] -= 1
                nova_planta = self.plantas_disponiveis[planta_selecionada]()
                self.plantas_plantadas.append(nova_planta)
                print(f"{planta_selecionada} plantada")
                if self.inventario[planta_selecionada] == 0:
                    del self.inventario[planta_selecionada]
            else:
                print("Planta inválida")

    def regar(self):
        if self.plantas_plantadas == []:
            print("Não tens plantas para regar")
        else:
            for planta in self.plantas_plantadas:
                planta.crescer()
    
    def recolher(self):
        if self.plantas_plantadas == []:
            print("Não tens plantas para recolher")
        else:
            for planta in self.plantas_plantadas:
                if planta.posso_recolher:
                    self.rendimento += planta.rendimento_colheita
                    planta.recolher()
                    self.plantas_plantadas.remove(planta)

    def procurar(self):
        planta_encontrada = random.choice(list(self.plantas_disponiveis.keys()))
        if planta_encontrada in self.inventario:
            self.inventario[planta_encontrada] += 1
        else:
            self.inventario[planta_encontrada] = 1
        print(f"Encontraste uma {planta_encontrada}")

    def mostrar_rendimento(self):
        print(f"O teu rendimento é de {self.rendimento}€")
