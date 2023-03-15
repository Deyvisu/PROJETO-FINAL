from flask import *
import requests
import psycopg2
from Modelos.classeUsuario import Usuario
from Modelos.classeEndereço import Endereço
from Modelos.classeCarrinho import Carrinho
from Modelos.classeLoja import Loja
from Modelos.classeProdutos import Produto
from Controle.classeConexao import Conexao

  
app = Flask(__name__, static_folder="static")

try:
    con = Conexao("MEIC", "localhost","5432","postgres","postgres")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro - ", error)


@app.route("/")
def home():
    return render_template('HomePage.html')


@app.route("/CadastroUsuario", methods = ("GET", "POST"))
def cadastrarCli():
    if request.method == "POST":
        usuario = Usuario("default", request.form['nomeCompleto'],request.form['dataNascimento'],request.form['cpf'],request.form['telefone'],request.form['email'],request.form['senha'])
        con.manipularBanco(usuario.inserirUsuario("Cadastro_Cliente"))

        resultado = con.consultarBanco(usuario.listarUsuario("Cadastro_Cliente"))

        return redirect(f'user/{resultado[0][0]}')

    else:
        return render_template('CadastroUsuario.html')
    

@app.route("/LoginUsuario", methods = ("GET", "POST"))
def loginCli():
    if request.method == "POST":
        usuario = Usuario(None, None, None, None, None, request.form['emailLogin'], request.form['senhaLogin'])
        resultado = con.consultarBanco(usuario.listarUsuario("Cadastro_Cliente"))
        if resultado == []:
            return render_template('LoginUsuario.html', mensagem = "Usuário não cadastrado!")
        else:
            return redirect(f'/user/{resultado[0][0]}')
    else:
        return render_template('LoginUsuario.html')


@app.route("/CadastroEndereço", methods = ("GET", "POST"))
def cadastroEnderço():
    if request.method == "POST":
        consultaUsuario = con.consultarBanco(f'''SELECT * FROM "Cadastro_Cliente" WHERE "CPF" = '{request.form["cpfUsuario"]}' ''')
        if consultaUsuario == []:
            return render_template('CadastroEndereço.html', mensagem = "Usuário não tem endereço cadastrado!")
        
        else:
            endereço = Endereço("default", request.form["cep"], request.form["nomeRua"], request.form["numeroEndereço"], request.form["complemento"], request.form["nomeBairro"], request.form["pontoReferencia"], request.form["cidade"], request.form["estado"], consultaUsuario[0][0])
            con.manipularBanco(endereço.inserirEndereço("Cadastro_Endereço"))
            return redirect(f'/user/{consultaUsuario[0][0]}')
                    
    
    else:
        return render_template('CadastroEndereço.html')
    

@app.route("/AlterarEndereco", methods= ("GET", "POST"))
def alterarEnd():
    if request.method == "POST":
        endereco = Endereço("default", request.form["cepAlterar"], request.form["nomeRuaAlterar"], request.form["numeroEnderecoAlterar"], request.form["complementoAlterar"], request.form["nomeBairroAlterar"], request.form["pontoReferenciaAlterar"], request.form["cidadeAlterar"], request.form["estadoAlterar"], None)
        con.manipularBanco(endereco.alterarEndereço("Cadastro_Cliente"))

        return render_template('ExibirEndereco.html')
    else:
        return render_template('AlterarEndereco.html')


@app.route("/user/<int:idUsuario>")
def verUsuario(idUsuario):
    id = int(idUsuario)
    usuario = Usuario(id, None, None, None, None, None, None)
    resultado = con.consultarBanco(usuario.listarUsuarioID("Cadastro_Cliente"))
    if resultado == []:
        return redirect("/HomePage") #pagina de erro
    else:
        return render_template('ExibirPerfilUsuario.html', dados = resultado )


@app.route("/user/<int:idUsuario>/ExibirEndereco")
def verEndereço(idUsuario):
    id = int(idUsuario)
    usuario = Usuario(id, None, None, None, None, None, None)
    resultado = con.consultarBanco(usuario.listarUsuarioID("Cadastro_Cliente"))
    resultadoEndereco = con.consultarBanco(f'''SELECT * FROM "Cadastro_Endereço" WHERE "ID_Cliente" = '{id}' ''')
    if resultado == []:
        return redirect("/ExibirPerfilUsuario")
    else:
        return render_template('ExibirEndereco.html', dadosEndereço = resultadoEndereco, dados = resultado)


@app.route("/ConfirmaçãoCPFAlterar", methods=("GET", "POST"))
def confirmaçãoAlterarUsuario():
    if request.method == "POST":
        usuario = Usuario(None, None, None, request.form["cpfConfirmação"], None, None, None)
        resultado = con.consultarBanco(usuario.confirmaçãoCPFUsuario("Cadastro_Cliente"))
        if resultado == []:
            return render_template('ConfirmaçãoCPFAlterar.html')
        else:
            return redirect('/AlterarUsuario')
    else:
        return render_template('ConfirmaçãoCPFAlterar.html')
    

@app.route("/ConfirmacaoCPFEnderecoAlterar", methods=("GET", "POST"))
def confirmaçãoAlterarEndereco():
    if request.method == "POST":
        usuario = Usuario(None, None, None, request.form["cpfConfirmação"], None, None, None)
        resultado = con.consultarBanco(usuario.confirmaçãoCPFUsuario("Cadastro_Cliente"))
        if resultado == []:
            return render_template('ConfirmacaoCPFEnderecoAlterar.html')
        else:
            return redirect('/AlterarEndereco')
    else:
        return render_template('ConfirmacaoCPFEnderecoAlterar.html')


@app.route("/AlterarUsuario", methods= ("GET", "POST"))
def alterarUsu():
    if request.method == "POST":
        usuario = Usuario("default", request.form["nomeCompletoAlterar"], request.form["dataNascimentoAlterar"], request.form["cpfAlterar"], request.form["telefoneAlterar"], request.form["emailAlterar"], request.form["senhaAlterar"])
        con.manipularBanco(usuario.alterarUsuario("Cadastro_Cliente"))

        return render_template('ExibirPerfilUsuario.html')
    else:
        return render_template('AlterarUsuario.html')


@app.route("/CadastroLojaLogin", methods=("GET", "POST"))
def verificacao():
    return render_template("CadastroLojaLogin.html")


@app.route("/CadastrarLoja", methods=("GET", "POST"))
def cadastroLoja():
    if request.method == "POST":
        loja = Loja("default", request.form["nomeLoja"], request.form["cnpj"], request.form["idEndereço"], request.form["cpf"])
        con.manipularBanco(loja.cadastrarLoja("Cadastro_Loja"))
        return render_template("HomePage.html")
    else:
        return render_template('CadastrarLoja.html')


@app.route("/user/<int:idUsuario>/MinhasLojas")
def verMinhasLojas(idUsuario):
    id = int(idUsuario)
    usuario = Usuario(id, None, None, None, None, None, None)
    resultado = con.consultarBanco(usuario.listarUsuarioID("Cadastro_Cliente"))
    resultadoMinhaLoja = con.consultarBanco(f'''SELECT * FROM "Cadastro_Loja" WHERE "CPF_Usuario" = '{resultado[0][3]}' ''')
    if resultado == []:
        return redirect("/ExibirPerfilUsuario")
    else:
        return render_template('MinhasLojas.html', dados = resultadoMinhaLoja)
    

@app.route("/MostrarLojas")
def mostrarLojas():
        todasLojas = Loja(None, None, None, None, None)
        resultado = con.consultarBanco(todasLojas.mostrarSobreAsLojas("Cadastro_Loja"))
        if resultado == []:
            return render_template("HomePage.html")
        else:
            return render_template("MostrarLojas.html", dados = resultado)


@app.route("/CadastrarProdutos", methods=("GET", "POST"))
def cadastrarProd():
    if request.method == "POST":
        produto = Produto("default", request.form["nomeProduto"], request.form["categoria"], request.form["quantidade"], request.form["preco"], request.form["idLoja"])
        con.manipularBanco(produto.cadastrarProduto("Cadastro_Produto"))
        resultadoProduto = con.consultarBanco(produto.listarProdutos("Cadastro_Produto"))
        if resultadoProduto == []:
            return redirect("/ExibirProdutos") #escrever mensagem que retornou vazio
        else:
            return redirect("/ExibirProdutos")
    else:
        return render_template("CadastrarProdutos.html") #escrever mensagem que tentou enviar vazio


@app.route("/VerificarIDLoja", methods=("GET", "POST"))
def verificarIDLoja():
    if request.method == "POST":
        loja = Loja(request.form["idLoja"], None, None, None, None)
        resultado = con.consultarBanco(loja.mostrarLojaID("Cadastro_Loja"))
        if resultado == []:
            return render_template("VerificarIDLoja.html") #mensagem de erro de ID vazio
        else:
            return redirect('/ExibirProdutos')
    else:
        return render_template("VerificarIDLoja.html") #mensagem de erro de ID de loja


@app.route("/ExibirProdutos")
def exibirProd():
    produtos = Produto(None, None, None, None, None, None)
    resultado = con.consultarBanco(produtos.listarProdutos("Cadastro_Produto"))

    return render_template('ExibirProdutos.html', dadosProduto = resultado)


@app.route("/DeletarProduto", methods=("GET", "POST"))
def deletarProd():
    if request.method == "POST":
        consultarProduto = Produto(request.form["idDeletar"], None, None, None, None, None)
        resultadoConsultarProduto = con.consultarBanco(consultarProduto.listarProdutoID("Cadastro_Produto"))
        if resultadoConsultarProduto == []:
            return render_template('ExibirProdutos.html') #colocar mensagem de que o id do produto n existe
        else: 
            produto = Produto(request.form["idDeletar"], None, None, None, None, None)
            con.manipularBanco(produto.deletarProduto("Cadastro_Produto"))
            resultado = con.consultarBanco(produto.listarProdutos("Cadastro_Produto"))

            return render_template("ExibirProdutos.html", dadosProduto = resultado) #colocar mensagem de que o produto foi deletado
    else:
        return render_template('DeletarProduto.html') #colocar mensagem de erro

@app.route("/Carrinho")
def mostrarCarrinho():
    render_template("Carrinho.html")


# Compra individual: Pagina, do Select dos produtos da loja, e um botao de fazer a compra(post, idCompra, a quantidade, id cliente, ). Campo quantidade, etc.


# LocalStorage para armazenar o ID dos produtos comprados
# Na pagina carrinho: Pegar ID guardado no LocalStorage e consultar o flask pra pegar as info dos produtos
# Criar rota "produtos/ID" que returne as informações do produto
# Salvar no javascript da pagina carrinho.html e usar as infos para imprimir os produtos no carrinho.

# @app.route("/loja/<int:idLoja>") uma pagina com o ID da loja, e posteriormente exibir o produto

     

if __name__== "__main__":
    app.run(debug=True)