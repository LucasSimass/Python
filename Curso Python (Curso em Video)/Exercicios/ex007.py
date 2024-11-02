n1 = float(input("Primeria nota do aluno: ")) 
n2 = float(input("Segunda nota do aluno: ")) 

media = (n1 + n2) / 2
print("-" * 20)

print(f"O aluno tem uma média de {media:.1f}")
print("-" * 20)

if media >= 5:
    print("O aluno passou!")
else:
    print("O aluno reprovou!")

