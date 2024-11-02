def quebraSenha(senha, alfabeto):
    for d in range(len(alfabeto)):
        for c in range(len(alfabeto)):
            for b in range(len(alfabeto)):
                for a in range(len(alfabeto)):
                    senhaTentativa =  alfabeto[d] + alfabeto[c] + alfabeto[b] + alfabeto[a]
                    if(senhaTentativa == senha):
                        print("A senha é: " + senhaTentativa)
                        return senhaTentativa
                        

senha = "9999"

alfabeto = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


quebraSenha(senha,alfabeto)