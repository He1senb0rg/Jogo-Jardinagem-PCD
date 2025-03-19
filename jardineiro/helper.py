class Helper:
    def __criar_lista_items(self, items):
        if type(items) == dict:
            self.item_list = list(items.keys())
        elif type(items) == list:
            self.item_list = items
        else:
            print("Tipo de item inválido.")
            return False
        return True
        
    def __lista_items(self):
        for i in range(len(self.item_list)):
            try:
                nome_item = self.item_list[i].nome
            except:
                nome_item = self.item_list[i]
            print(f"{i + 1}. {nome_item}")

    def __obter_seleccao_utilizador(self):
        while True:
            input_utilizador = input("Seleciona um item: ")
            try:
                input_utilizador = int(input_utilizador)
                if 0 < input_utilizador and input_utilizador <= len(self.item_list):
                    return self.item_list[input_utilizador - 1]
                else:
                    print("Input inválido.")
            except:
                print("Input inválido.")

    def seleccionar_item(self, items):
        if self.__criar_lista_items(items):
            self.__lista_items()
            seleccao = self.__obter_seleccao_utilizador()
            return seleccao

        