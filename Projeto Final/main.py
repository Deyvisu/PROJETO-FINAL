from flask import *
import psycopg2
from Modelos.classeUsuario import Usuario
from Modelos.classeEndereço import Endereço
from Modelos.classeCarrinho import Carrinho
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
        usuario = Usuario("default", request.form['nomeCompleto'],request.form['idade'],request.form['dataNascimento'],request.form['cpf'],request.form['telefone'],request.form['email'],request.form['senha'])
        con.manipularBanco(usuario.inserirUsuario("Cadastro_Cliente"))

        return render_template('HomePage.html')

    else:
        return render_template('CadastroUsuario.html')
    

@app.route("/LoginUsuario", methods = ("GET", "POST"))
def loginCli():
    if request.method == "POST":
        usuario = Usuario(None, None, None, None, None, None, request.form['emailLogin'], request.form['senhaLogin'])
        resultado = con.consultarBanco(usuario.listarUsuario("Cadastro_Cliente"))
        endereço = Endereço(None, None, None, None, None, None, None, None, None, resultado[0][0])
        resultadoEndereço = con.consultarBanco(endereço.listarEndereçoPorIDUsuario("Cadastro_Endereço"))
        if resultado == []:
            return render_template('LoginUsuario.html')
        else:
            return render_template('ExibirPerfilUsuario.html', dados = resultado, dadosEndereço = resultadoEndereço)
    else:
        return render_template('LoginUsuario.html')


@app.route("/CadastroEndereço", methods = ("GET", "POST"))
def cadastroEnderço():
    if request.method == "POST":
        endereço = Endereço("default", request.form["cep"], request.form["nomeRua"], request.form["numeroEndereço"], request.form["complemento"], request.form["nomeBairro"], request.form["pontoReferencia"], request.form["cidade"], request.form["estado"], request.form["idUsuario"])
        con.manipularBanco(endereço.inserirEndereço("Cadastro_Endereço"))

        return render_template('ExibirPerfilUsuario.html')
    
    else:
        return render_template('CadastroEndereço.html')

@app.route("/ConfirmaçãoCPFAlterar", methods=("GET", "POST"))
def confirmaçãoAlterarUsuário():
    if request.method == "POST":
        usuario = Usuario(None, None, None, None, request.form["cpfConfirmação"], None, None, None)
        resultado = con.consultarBanco(usuario.confirmaçãoCPFUsuario("Cadastro_Cliente"))
        if resultado == []:
            return render_template('ConfirmaçãoCPFAlterar.html')
        else:
            return redirect('/AlterarUsuário')
    else:
        return render_template('ConfirmaçãoCPFAlterar.html')
    
@app.route("/ConfirmaçãoCPFDeletar", methods=("GET", "POST"))
def confirmaçãoDeletarUsuário():
    if request.method == "POST":
        usuario = Usuario(None, None, None, None, request.form["cpfConfirmaçãoDeletar"], None, None, None)
        resultado = con.consultarBanco(usuario.confirmaçãoCPFUsuario("Cadastro_Cliente"))
        if resultado == []:
            return render_template('ConfirmaçãoCPFDeletar.html')
        else:
            return redirect('/DeletarUsuário')
    else:
        return render_template('ConfirmaçãoCPFDeletar.html')

@app.route("/AlterarUsuário", methods= ("GET", "POST"))
def alterarUsu():
    if request.method == "POST":
        usuario = Usuario("default", request.form["nomeCompletoAlterar"], request.form["idadeAlterar"], request.form["dataNascimentoAlterar"], request.form["cpfAlterar"], request.form["telefoneAlterar"], request.form["emailAlterar"], request.form["senhaAlterar"])
        con.manipularBanco(usuario.alterarUsuario("Cadastro_Cliente"))

        return render_template('ExibirPerfilUsuario.html')
    else:
        return render_template('AlterarUsuário.html')


@app.route("/DeletarUsuário", methods=("GET", "POST"))
def deletarUsu():
    if request.method == "POST":
        usuario = Usuario("default", None, None, None, None, None, request.form["emailDeletar"], request.form["senhaDeletar"])
        con.manipularBanco(usuario.DeletarUsuario("Cadastro_Cliente"))

        return render_template('HomePage.html')
    else:
        return render_template('DeletarUsuário.html')
    

@app.route("/Carrinho", methods=("GET", "POST"))
def mostrarCarrinho():
    if request.method == "POST":
        carrinho = Carrinho(None, None, None, None, None, None)
        resultado = con.consultarBanco(carrinho.mostrarCarrinho("Carrinho"))
        if resultado == []:
            return render_template('')
        else:
            return render_template('', carrinho = resultado)
    else:
        return render_template('')
     

if __name__== "__main__":
    app.run(debug=True)