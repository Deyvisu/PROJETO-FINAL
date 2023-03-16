let lista = []

let novoItem = document.querySelector('#novoItem');
let btnNovoItem = document.querySelector('#btnNovoItem');
let itens = document.querySelector('#itens');

btnNovoItem.addEventListener('click', () => {
    inserirItem({ nome: novoItem.value, id: gerarID }) //esse 'null' tem q ser substituido por um identificador do proprio banco de dados, ou algo que referencie ele no codigo
    novoItem.value = '';
})

function gerarID() {
    return Math.floor(Math.random() * 8000);
}

function inserirItem(item, novoItem = true){
    lista.push(item);
    itens.appendChild(criarItemLista(item));
    if(novoItem) {
        sessionStorage.setItem('listaDeCompras', JSON.stringify(lista));
    }
}

function criarItemLista(item) {

    let li = document.createElement('li');
    let btnHtml = '<button onClick="deletarItem('+item.id+')">Deletar</button>';
    li.innerHTML = item.nome + '&nbsp;&nbsp;' + btnHtml;
    li.style.marginBotton = '15px';
    li.id = item.id;
    return li;
}

