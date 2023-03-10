class Loja:
    def __init__(self, idLoja, nomeLoja, cnpj, idEndereço, idUsuario):
        self._idLoja = idLoja
        self._nomeLoja = nomeLoja
        self._cnpj = cnpj
        self._idEndereço = idEndereço
        self._idUsuario = idUsuario


    def cadastrarLoja(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        VALUES ('{self._idLoja}', '{self._nomeLoja}', '{self._cnpj}', '{self._idEndereço}', '{self._idUsuario}') '''

        return sql
    
    def mostrarSobreAsLojas(self, tabela):
        sql = f'''
        SELECT * FROM "{tabela}" ORDER BY "Nome da Loja" ASC'''

        return sql
    
    def alterarLoja(self, tabela):
        sql = f'''
        UPDATE "{tabela}"
        SET "Nome da Loja" = '{self._nomeLoja}', "CNPJ" = '{self._cnpj}', "ID do Endereço" = '{self._idEndereço}', "ID do Usuario" = '{self._idUsuario}'
        WHERE "Nome da Loja" = '{self._nomeLoja}'
        '''
        return sql

    def excluirLoja(self, tabela):
        sql = f'''
        DELETE FROM "{tabela}"
        WHERE "Nome da Loja" = '{self._nomeLoja}' '''

        return sql