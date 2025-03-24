import random
from .helper import Helper
from plantas.alface import Alface
from plantas.cenoura import Cenoura
from plantas.tomate import Tomate
from plantas.batata import Batata
from items.fertelizante import Fertelizante

class Jardineiro:
    """Representa um jardineiro que pode plantar, regar e recolher plantas."""

    def __init__(self, nome):
        self.nome = nome
        self.plantas_plantadas = []
        self.inventario = {}
        self.inventario_items = []
        self.plantas_disponiveis = {"tomate": Tomate, "alface": Alface, "cenoura": Cenoura, "batata": Batata}
        self.items_disponiveis = {"fertelizante": Fertelizante}
        self.rendimento = 10

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
    
    def recolher(self): #por alguma razao so ta a recolher uma planta?????
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

    def mostrar_inventario(self):
        if self.inventario_items == {}:
            print("Não tens items no inventário")
        else:
            item_selecionado = Helper().seleccionar_item(self.inventario_items)
               
            if self.plantas_plantadas == []:
                print("Não tens plantas para aplicar o item")
            else:
                planta_selecionada = Helper().seleccionar_item(self.plantas_plantadas)
                item_selecionado.aplicar(planta_selecionada)
                self.inventario_items.remove(item_selecionado)
    
    def loja(self):
        print("Items disponíveis:")
        item_selecionado = Helper().seleccionar_item(self.items_disponiveis) # ainda nao aparece o preço dos items
        if self.rendimento < self.items_disponiveis[item_selecionado]().preco:
            print("Não tens dinheiro suficiente")
        else:
            self.rendimento -= self.items_disponiveis[item_selecionado]().preco
            novo_item = self.items_disponiveis[item_selecionado]()
            self.inventario_items.append(novo_item)
            
            print(f"Compraste {item_selecionado}!")

