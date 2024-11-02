function clicou(){
    tabela = document.getElementById('tabela')


    tr = document.createElement('tr')
    nome = document.getElementById("nome")
    idade = document.getElementById("idade")
    nome = nome.value
    idade = idade.value

    
    td1 = document.createElement("td")
    td2 = document.createElement("td")

    td1.innerHTML = nome
    td2.innerHTML = idade


    tabela.appendChild(tr)
    tr.appendChild(td1)
    tr.appendChild(td2)


    nome = document.getElementById("nome")
    idade = document.getElementById("idade")

   if (nome){
    nome.value = ""
   }
   if (idade){
    idade.value = ""
   }
}


