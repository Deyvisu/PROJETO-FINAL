class Produto:
    def __init__(self, idProduto, nomeProduto, categoria, quantidade, preçoUnit, idLoja):
        self._idProduto = idProduto
        self._nomeProduto = nomeProduto
        self._categoria = categoria
        self._quantidade = quantidade
        self._preçoUnit = preçoUnit
        self._idLoja = idLoja

    def cadastrarProduto(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        Values({self._idProduto},'{self._nomeProduto}','{self._categoria}','{self._quantidade}', '{self._preçoUnit}', '{self._idLoja}')
        '''
        return sql
    
    def listarProdutos(self, tabela):
        sql = f'''
        SELECT * FROM "{tabela}" ORDER BY "ID" ASC '''
        return sql
    
    def listarProdutoID(self, tabela):
        sql = f'''
        SELECT * FROM "{tabela}" WHERE "ID" = {self._idProduto} '''
        return sql

    def alterarProduto(self, tabela):
        sql = f'''
        UPDATE "{tabela}"
        SET "Nome" = '{self._nomeProduto}', "Categoria" = '{self._categoria}', "Quantidade" = '{self._quantidade}', "Preço" = '{self._preçoUnit}'
        WHERE "Nome" = '{self._nomeProduto}'
        '''
        return sql
    
    def deletarProduto(self, tabela):

        sql = f'''
        DELETE FROM "{tabela}"
        WHERE "ID" = {self._idProduto}
        '''
        return sql