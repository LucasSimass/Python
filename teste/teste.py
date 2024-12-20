def quebraSenha(senha, alfabeto):
    for e in range(len(alfabeto)):
        for d in range(len(alfabeto)):
            for c in range(len(alfabeto)):
                for b in range(len(alfabeto)):
                    for a in range(len(alfabeto)):
                        senhaTentativa =  alfabeto[e] + alfabeto[d] + alfabeto[c] + alfabeto[b] + alfabeto[a]
                        if(senhaTentativa == senha):
                            print("A senha é: " + senhaTentativa)
                            return senhaTentativa
                        

senha = "2o05b"

alfabeto = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z","0","1","2","3","4","5","6","7","8","9"]

quebraSenha(senha,alfabeto)
