import datetime
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal

class NotaFiscal():
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente
        self._data=datetime.datetime.today()
        self._itens=[]
        self._valorNota=0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = + item._valorItem
        self.valorNota = valor

    def imprimirNotaFiscal(self):
        print('-' * 112)
        print(
            "NOTA FISCAL                                                                                          {}/{}/{}".format(
                self._data.day, self._data.month, self._data.year))
        print("Cliente: ", self._Id, " Nome:", self._cliente._nome)
        print("CPF/CNPJ: ", self._cliente._cnpjcpf)
        print('-' * 112)
        print('ITENS')
        print('-' * 112)
        print(
            "Seq    Descrição                                                 QTD         Valor Unit            Preço")
        print('-'* 4, '-' * 54, '  -'* 5, '      -'* 12,
              '    -'* 18)

