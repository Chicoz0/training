class Cliente():
    def __init__(self, cpf: str, nome: str, endereco: str, telefone: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf: str):
        self.__cpf = novo_cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco: str):
        self.__endereco = novo_endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone
