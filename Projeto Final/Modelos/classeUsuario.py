class Usuario:

    def __init__(self,id,nomeCompleto,dataNasc,cpf,telefone,email,senha):
        self._id = id
        self._nomeCompleto = nomeCompleto
        self._dataNasc = dataNasc
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
        self._senha = senha

    def inserirUsuario(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        Values({self._id},'{self._nomeCompleto}','{self._dataNasc}', '{self._cpf}', '{self._telefone}', '{self._email}', '{self._senha}')
        '''

        return sql
    
    def listarUsuario(self, tabela):
        
        sql = f'''
        SELECT * FROM "{tabela}" 
        WHERE "E-mail" = '{self._email}' and "Senha" = '{self._senha}'
        
        '''
        return sql
    
    def listarUsuarioID(self, tabela):
        
        sql = f'''
        SELECT * FROM "{tabela}" 
        WHERE "ID" = '{self._id}'
        
        '''
        return sql
    
    def confirmaçãoCPFUsuario(self, tabela):

        sql = f'''
        SELECT * FROM "{tabela}"
        WHERE "CPF" = '{self._cpf}'
        '''

        return sql

    def DeletarUsuario(self, tabela):

        sql = f'''
        DELETE FROM "{tabela}"
        WHERE "E-mail" = '{self._email}' and "Senha" = '{self._senha}'
        
        '''
        return sql
    
    def alterarUsuario(self, tabela):

        sql = f'''
        UPDATE "{tabela}"
        SET "Nome Completo" = '{self._nomeCompleto}', "Data Nascimento" = '{self._dataNasc}', "CPF" = '{self._cpf}', "Telefone" = '{self._telefone}', "E-mail" = '{self._email}', "Senha" = '{self._senha}'
        WHERE "CPF" = '{self._cpf}'
        '''
        return sql

    def imprimirUsuario(self):
    
        return f'''
    Usuario:
    ID: {self._id}
    Nome Completo do Usuario: {self._nomeCompleto}
    Data do Nascimento: {self._dataNasc}
    CPF: {self._cpf}
    Telefone: {self._telefone}
    E-mail: {self._email}
    Senha: {self._senha}
        
        '''