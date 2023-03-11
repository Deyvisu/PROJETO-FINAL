class Loja:
    def __init__(self, idLoja, nomeLoja, cnpj, idEndereço, cpfUsuario):
        self._idLoja = idLoja
        self._nomeLoja = nomeLoja
        self._cnpj = cnpj
        self._idEndereço = idEndereço
        self._cpfUsuario = cpfUsuario


    def cadastrarLoja(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        VALUES ('{self._idLoja}', '{self._nomeLoja}', '{self._cnpj}', '{self._idEndereço}', '{self._cpfUsuario}') '''

        return sql
    
    def mostrarSobreAsLojas(self, tabela):
        sql = f'''
        SELECT * FROM "{tabela}" ORDER BY "Nome" ASC'''

        return sql
    
    def alterarLoja(self, tabela):
        sql = f'''
        UPDATE "{tabela}"
        SET "Nome" = '{self._nomeLoja}', "CNPJ" = '{self._cnpj}', "ID_Endereço" = '{self._idEndereço}', "CPF do Usuario" = '{self._cpfUsuario}'
        WHERE "Nome" = '{self._nomeLoja}'
        '''
        return sql

    def excluirLoja(self, tabela):
        sql = f'''
        DELETE FROM "{tabela}"
        WHERE "Nome" = '{self._nomeLoja}' '''

        return sql