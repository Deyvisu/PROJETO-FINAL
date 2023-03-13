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
    
    
@app.route("/ConfirmaçãoCPFDeletar", methods=("GET", "POST"))
def confirmaçãoDeletarUsuario():
    if request.method == "POST":
        usuario = Usuario(None, None, None, request.form["cpfConfirmaçãoDeletar"], None, None, None)
        resultado = con.consultarBanco(usuario.confirmaçãoCPFUsuario("Cadastro_Cliente"))
        if resultado == []:
            return render_template('ConfirmaçãoCPFDeletar.html')
        else:
            return redirect('/DeletarUsuario')
    else:
        return render_template('ConfirmaçãoCPFDeletar.html')

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


@app.route("/DeletarUsuario", methods=("GET", "POST"))
def deletarUsu():
    if request.method == "POST":
        usuario = Usuario("default", None, None, None, None, request.form["emailDeletar"], request.form["senhaDeletar"])
        con.manipularBanco(usuario.DeletarUsuario("Cadastro_Cliente"))

        return render_template('HomePage.html')
    else:
        return render_template('DeletarUsuario.html')

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
    
@app.route("/MostrarLojas")
def mostrarLojas():
        todasLojas = Loja(None, None, None, None, None)
        resultado = con.consultarBanco(todasLojas.mostrarSobreAsLojas("Cadastro_Loja"))
        if resultado == []:
            return render_template("HomePage.html")
        else:
            return render_template("MostrarLojas.html", dados = resultado)

# @app.route("/Carrinho", methods=("GET", "POST"))
# def mostrarCarrinho():
#     if request.method == "POST":
#         carrinho = Carrinho(None, None, None, None, None, None)
#         resultado = con.consultarBanco(carrinho.mostrarCarrinho("Carrinho"))
#         if resultado == []:
#             return render_template('')
#         else:
#             return render_template('', carrinho = resultado)
#     else:
#         return render_template('')
     

if __name__== "__main__":
    app.run(debug=True)