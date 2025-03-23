class Planta:
    def __init__(self, nome, rendimento_colheita):
        self.nome = nome
        self.estado_crescimento = ["semente", "rebento", "madura", "flor", "fruta", "pronto-recolher"]
        self.__estado_atual = 0
        self.__pronto_recolher = False
        self.rendimento_colheita = rendimento_colheita

    def crescer(self):
        if not self.__pronto_recolher:
            self.__estado_atual += 1
            print(f"{self.nome} cresceu para {self.obter_nome_estado_actual()}")

            if self.__estado_atual == len(self.estado_crescimento) - 1:
                print(f"{self.nome} já está pronto para recolher")
                self.__pronto_recolher = True
        else:
            print(f"{self.nome} já está pronto para recolher")

    def recolher(self):
        if self.__pronto_recolher:
            print(f"{self.nome} foi colhida, recebeste {self.rendimento_colheita}€ de rendimento")
            self.__estado_atual = 0
            self.nome_estado_atual = self.estado_crescimento[0]
            self.__pronto_recolher = False
        else:
            print(f"{self.nome} ainda não está pronto para recolher")
    
    def obter_nome_estado_actual(self):
        return self.estado_crescimento[self.__estado_atual]
    
    @property
    def posso_recolher(self):
        return self.__pronto_recolher