class ItemPedido():
    def __init__(self, codigo: int, descricao: str,
                 preco_unitario: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco_unitario = preco_unitario

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nova_codigo: int):
        self.__codigo = nova_codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao: str):
        self.__descricao = nova_descricao

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, nova_preco_unitario: float):
        self.__preco_unitario = nova_preco_unitario