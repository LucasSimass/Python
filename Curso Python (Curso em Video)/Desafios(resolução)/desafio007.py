nome = input("Nome do aluno: ").capitalize()

nota1 = float(input(f"Primera nota do aluno, {nome}: "))
nota2 = float(input(f"Segunda nota do aluno, {nome}: "))

media = (nota1 + nota2) / 2

print(f"A media do {nome} é {media}!")

if media >= 5.0:
    print(f"O {nome} passou de ano!")
else:
    print(f"O {nome} foi reprovado!")