//Variáveis
const button = document.querySelector(".button");
const inputNome = document.querySelector("#nome");
const inputEmail = document.querySelector("#email");

//Criando elemento 'p' para o erro
const error = document.createElement('p');

//Função de limpeza de dados do input
function clearForm() {
    error.textContent = '';
    inputNome.value = '';
    inputEmail.value = '';

}

//Criando evento de click para a validação
button.addEventListener(("click"), function(event){
    event.preventDefault();
    
    //validação

    //Nome
    if (inputNome.value.trim() === ''){
        error.textContent = "Campo Obrigatório";
        inputNome.insertAdjacentElement('afterend', error);
        error.setAttribute('class', 'error');
        return false;
    }
    //Email
    if (inputEmail.value.trim() === ''){
        error.textContent = "Campo Obrigatório";
        inputEmail.insertAdjacentElement('afterend', error);
        error.setAttribute('class', 'error');
        return false
    }

   clearForm(); 
})