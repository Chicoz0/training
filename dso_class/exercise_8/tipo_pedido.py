class TipoPedido():

    def __init__(self, descricao: str, fator_distancia: float):
        self.__descricao = descricao
        self.__fator_distancia = fator_distancia

    @property
    def descricao(self):
        return self.__descricao

    @property
    def fator_distancia(self):
        return self.__fator_distancia

    @descricao.setter
    def descricao(self, nova_descricao: str):
        self.__descricao = nova_descricao

    @fator_distancia.setter
    def fator_distancia(self, nova_fator_distancia: float):
        self.__fator_distancia = nova_fator_distancia
