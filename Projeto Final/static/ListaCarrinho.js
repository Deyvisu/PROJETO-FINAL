let lista = JSON.parse(localStorage.getItem('listaDeCompras'))

let novoItem = document.querySelector('#novoItem');
let btnNovoItem = document.querySelector('#btnNovoItem');
let itens = document.querySelector('#itens');

btnNovoItem.addEventListener('click', () => {
    inserirItem({ nome: novoItem.value, id: gerarID() }) //esse 'null' tem q ser substituido por um identificador do proprio banco de dados, ou algo que referencie ele no codigo
    novoItem.value = '';
})

function gerarID() {
    return Math.floor(Math.random() * 8000);
}

function inserirItem(item, novoItem = true){
    lista.push(item);
    itens.appendChild(criarItemLista(item));
    if(novoItem) {
        localStorage.setItem('listaDeCompras', JSON.stringify(lista));
    }
}


function renderizarLocalStorage(chaveLocalStorage){

    const colecao = JSON.parse(localStorage.getItem(chaveLocalStorage));

    colecao.forEach(element => {

        itens.appendChild(criarItemLista(element));
        
    });

    return true
}


function criarItemLista(item) {

    let li = document.createElement('li');
    let btnHtml = '<button onClick="deletarItem('+item['id']+')">Deletar</button>';
    li.innerHTML = item['nome'] + '&nbsp;&nbsp;' + btnHtml;
    li.style.marginBotton = '15px';
    li.id = item.id;
    return li;
}

// Ao entrar no carrinho, o codigo deve puxar a lista de compras do localStorage. Dentro do HTML utilizar a função que retorne o localStorage.

// passo a passo: passar a chave, e o get localstorage, se essa lista existir retornar ela na função, se não existir, returnar um n existe.

// 