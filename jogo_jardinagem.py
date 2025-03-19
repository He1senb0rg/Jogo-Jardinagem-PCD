from jardineiro.jardineiro import Jardineiro

class Jogo:
    def __init__(self):
        self.comandos = ["plantar", "regar", "recolher", "procurar", "ajuda", "sair"]
        nome_jardineiro = input("Qual é o teu nome? ")
        print(f"Bem-vindo ao jogo de Jardinagem, {nome_jardineiro}! Inicia escrevendo ajuda para uma lista de comandos.")
        self.jardineiro = Jardineiro(nome_jardineiro)

    def iniciar_jogo(self):
        while True:
            accao_jogador = input("O que desejas fazer? ")
            accao_jogador = accao_jogador.lower()
            if accao_jogador in self.comandos:
                if accao_jogador == "plantar":
                    self.jardineiro.plantar()
                elif accao_jogador == "regar":
                    self.jardineiro.regar()
                elif accao_jogador == "recolher":
                    self.jardineiro.recolher()
                elif accao_jogador == "procurar":
                    self.jardineiro.procurar()
                elif accao_jogador == "ajuda":
                    print("*** Comandos ***")
                    for command in self.comandos:
                        print(command)
                elif accao_jogador == "sair":
                    print("Adeus.")
                    break
            else:
                print("Comando inválido")

if __name__ == "__main__":
    Jogo().iniciar_jogo()