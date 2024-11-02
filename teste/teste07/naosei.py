import random 
palavras = ["Abacaxi", "abacate", "abelha", "abrigo", "abrir", "água", "alface", "além", "algodão", "alma", "altura", "amarelo", "amigo", "amor", "âncora", "anjo", "ano", "antecipação", "antigo", "aparência", "apertar", "apito", "aplausos", "aproveitar", "aquecer", "árvore", "areia", "aroma", "arroz", "asa", "assento", "astronauta", "azul", "bacia", "bailar", "banheira", "barata", "barco", "barulho", "bebê", "beijo", "biblioteca", "bicicleta", "binocular", "biscoito", "branco", "brilho", "brincar", "brisa", "broto", "café", "cabelo", "cachimbo", "cachorro", "caderno", "cadeira", "caixinha", "calça", "caminho", "campainha", "campo", "cantar", "canto", "capa", "capítulo", "caramba", "carne", "carnaval", "carro", "casaco", "casamento", "cascata", "castelo", "cata-vento", "céu", "celular", "cena", "centelha", "central", "cerveja", "cérebro", "chave", "cheiro", "chuva", "cidade", "cinema", "círculo", "cobertor", "coelho", "coisa", "colher", "colar", "colina", "combustível", "começar", "comida", "comportamento", "computador", "concha", "concurso", "confete", "confuso", "conhecimento", "conselho", "contar", "contrato", "corações", "corda", "correr", "cortiça", "cozinha", "cotovelo", "couro", "covil", "cozinha", "cratera", "criança", "cromo", "cruz", "cuco", "cultura", "cupido", "cura", "curva", "cuspir", "daqui", "dedo", "defesa", "degrau", "dente", "depressa", "descoberta", "desejo", "desenho", "desfile", "destino", "detector", "diabo", "diamante", "diário", "diferença", "dificuldade", "dinheiro", "direito", "disfarce", "dispositivo", "distância", "diversão", "dividir", "dobrar", "doces", "dor", "dormir", "dossel", "dragão", "duplo", "duração", "durante", "duvida", "dwelf", "efeito", "eixo", "elétrico", "elefante", "elenco", "embaixada", "embalagem", "emboscada", "emoção", "empada", "empenho", "encanto", "encontrar", "energia", "enigma", "entrada", "enviado", "equipe", "escada", "escolher", "esconderijo", "escrever", "escuro", "esfera", "esfregar", "esquilo", "escolha"]


escolhedor = random.randint(0,99)
quantidade_letras = len(palavras[escolhedor])

escolhedor2 = random.randint(0, quantidade_letras - 1)

palavra = palavras[escolhedor]


contador = 0


print(f"A palavra possui {quantidade_letras} letras")
print("*" * quantidade_letras)
print(f" Na posição {escolhedor2 + 1} da palavra tem a letra {palavra[escolhedor2]}")

if palavra[escolhedor2] == palavra[0]:
    print(1)

if (palavra):
    print(palavra)

for item in palavras:
    if (len(item) < 4 ):
        print("-" * 20)
        print(len(item))
