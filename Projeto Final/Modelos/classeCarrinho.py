class Carrinho:
    def __init__(self, preço, quantidade, idProduto, nomeProduto, idLoja, nomeLoja, idUsuario):
        self._preço = preço
        self._quantidade = quantidade
        self._idProduto = idProduto
        self._nomeProduto = nomeProduto
        self._idLoja = idLoja
        self._nomeLoja = nomeLoja
        self._idUsuario = idUsuario

    def adicionarItem(self, tabela):

        sql = f'''
        INSERT INTO "{tabela}"
        VALUES ({self._idProduto}, '{self._nomeProduto}', '{self._preço}', '{self._quantidade}', '{self._idLoja}', '{self._idUsuario}' '''

        return sql
    
    def removerItem(self, tabela):

        sql = f'''
        DELETE FROM "{tabela}"
        WHERE "ID_Produto" = '{self._idProduto}' '''

        return sql
    
    def mostrarCarrinho(self, tabela):

        sql = f'''
        SELECT * FROM "{tabela}" ORDER BY 'Preço' ASC
        '''

        return sql
    
    def preçoTotal(self, tabela):

        sql = f'''
        SELECT SUM '{self._preço}' FROM "{tabela}" '''

        return sql
        
    
    