// essa classe nos dá acesso a funcionalidade do ajax para recuperar alguma informação de algum servidor
var xhr = new XMLHttpRequest();

// buscando dados de usuário no Github
//xhr.open('GET', 'https://api.github.com/users/amaurirg');
xhr.open('GET', 'https://viacep.com.br/ws/11704420/json');
xhr.send(null);

// como a requisição não acontece no mesmo fluxo do script por ser assíncrona o JS
// não pode ficar esperando essa requisição finalizar para continuar o código. Para
// isso usamos o onreadystatechange
xhr.onreadystatechange = function() {
    // readyState === 4 onde o 4 significa quando a resposta retornou
    if(xhr.readyState === 4) {
        // mostra o retorno convertido de JSON para vetor
        console.log(JSON.parse(xhr.responseText));
        const {logradouro, uf} = JSON.parse(xhr.responseText)
        console.log(logradouro)
    }
}