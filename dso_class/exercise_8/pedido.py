from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tipo(self):
        return self.__tipo

    @property
    def itens(self):
        return self.__itens

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero

    @cliente.setter
    def cliente(self, novo_cliente):
        self.__cliente = novo_cliente

    @tipo.setter
    def tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    def inclui_item_pedido(self, codigo, descricao, preco):
        presente = False
        for item in self.__itens:
            if item.codigo == codigo:
                presente = True
                break
        if presente:
            return None
        else:
            item_pedido = ItemPedido(codigo, descricao, preco)
            self.__itens.append(item_pedido)
            return item_pedido

    def exclui_item_pedido(self, codigo):
        for item in self.__itens:
            if item.codigo == codigo:
                self.__itens.remove(item)
                return item
        return None

    def calcula_valor_pedido(self, distancia: float):
        preco_dos_itens = 0.0
        for item in self.__itens:
            preco_dos_itens += item.preco
        preco_total = (distancia * self.__tipo.fator_distancia) + preco_dos_itens
        if isinstance(self.__cliente, ClienteFidelidade):
            preco_total = preco_total * (1 - self.__cliente.desconto)
        return preco_total