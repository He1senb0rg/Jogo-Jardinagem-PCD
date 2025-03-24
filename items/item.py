class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} | {self.preco}€ | Qnt.: {self.quantidade}'