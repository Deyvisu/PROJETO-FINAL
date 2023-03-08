from flask import *
import psycopg2
from Modelos.classeCliente import Cliente
from Modelos.classeEndereço import Endereço
from Controle.classeConexao import Conexao


app = Flask(__name__)

try:
    con = Conexao("MEIC", "localhost","5432","postgres","postgres")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro - ", error)



@app.route("/")
def home():
    return render_template('HomePage.html')

@app.route("/CadastroCliente", methods = ("GET", "POST"))
def cadastrarCli():
    if request.method == "POST":
        usuario = Cliente("default", request.form['nomeCompleto'],request.form['idade'],request.form['dataNascimento'],request.form['cpf'],request.form['telefone'],request.form['email'],request.form['senha'])
        con.manipularBanco(usuario.inserirCliente("Cadastro_Cliente"))

        return render_template('HomePage.html')

    else:
        return render_template('CadastroCliente.html')
    

@app.route("/LoginCliente", methods = ("GET", "POST"))
def loginCli():
    if request.method == "POST":
        usuario = Cliente(None, None, None, None, None, None, request.form['emailLogin'], request.form['senhaLogin'])
        resultado = con.consultarBanco(usuario.listarCliente("Cadastro_Cliente"))
        endereço = Endereço(None, None, None, None, None, None, None, None, None, resultado[0][0])
        resultadoEndereço = con.consultarBanco(endereço.listarEndereçoPorIDUsuario("Cadastro_Endereço"))
        if resultado == []:
            return render_template('LoginCliente.html')
        else:
            return render_template('ExibirPerfilCliente.html', dados = resultado, dadosEndereço = resultadoEndereço)
    else:
        return render_template('LoginCliente.html')


@app.route("/CadastroEndereço", methods = ("GET", "POST"))
def cadastroEnderço():
    if request.method == "POST":
        endereço = Endereço("default", request.form["cep"], request.form["nomeRua"], request.form["numeroEndereço"], request.form["complemento"], request.form["nomeBairro"], request.form["pontoReferencia"], request.form["cidade"], request.form["estado"], request.form["idCliente"])
        con.manipularBanco(endereço.inserirEndereço("Cadastro_Endereço"))

        return render_template('ExibirPerfilCliente.html')
    
    else:
        return render_template('CadastroEndereço.html')

@app.route("/ConfirmaçãoCPFAlterar", methods=("GET", "POST"))
def confirmaçãoAlterarUsuário():
    if request.method == "POST":
        usuario = Cliente(None, None, None, None, request.form["cpfConfirmação"], None, None, None)
        resultado = con.consultarBanco(usuario.confirmaçãoCPFUsuário("Cadastro_Cliente"))
        if resultado == []:
            return render_template('ConfirmaçãoCPFAlterar.html')
        else:
            return redirect('/AlterarUsuário')
    else:
        return render_template('ConfirmaçãoCPFAlterar.html')
    
@app.route("/ConfirmaçãoCPFDeletar", methods=("GET", "POST"))
def confirmaçãoDeletarUsuário():
    if request.method == "POST":
        usuario = Cliente(None, None, None, None, request.form["cpfConfirmaçãoDeletar"], None, None, None)
        resultado = con.consultarBanco(usuario.confirmaçãoCPFUsuário("Cadastro_Cliente"))
        if resultado == []:
            return render_template('ConfirmaçãoCPFDeletar.html')
        else:
            return redirect('DeletarUsuário.html')
    else:
        return render_template('ConfirmaçãoCPFDeletar.html')

@app.route("/AlterarUsuário", methods= ("GET", "POST"))
def alterarUsu():
    if request.method == "POST":
        usuario = Cliente("default", request.form["nomeCompletoAlterar"], request.form["idadeAlterar"], request.form["dataNascimentoAlterar"], request.form["cpfAlterar"], request.form["telefoneAlterar"], request.form["emailAlterar"], request.form["senhaAlterar"])
        con.manipularBanco(usuario.alterarCliente("Cadastro_Cliente"))

        return render_template('ExibirPerfilCliente.html')
    else:
        return render_template('AlterarUsuário.html')


@app.route("/DeletarUsuário", methods=("GET", "POST"))
def deletarUsu():
    if request.method == "POST":
        usuario = Cliente("default", None, None, None, None, None, request.form["emailDeletar"], request.form["senhaDeletar"])
        con.manipularBanco(usuario.DeletarCliente("Cadastro_Cliente"))

        return render_template('HomePage.html')
    else:
        return render_template('/DeletarUsuário')
    

if __name__== "__main__":
    app.run(debug=True)