alunos_e_notas = [
    # (alunos, notas)
    ("A",3),
    ("B", 7),
    ("C", 6),
    ("D", 5),
    ("E", 4)
    ]

notas = [alunos_e_notas[i][1] for i in range(len(alunos_e_notas))]

def media(notas: list[float]) -> float:
    return (sum(notas) / len(notas))

def desvios(notas: list[float]) -> list[float]:
    return [nota - media(notas) for nota in notas]

print(media(notas))

print(sorted(desvios(notas)))

def variance(desvios_notas: list[float]) -> float:
    return sum(x * x for x in desvios_notas) / len(desvios_notas)

print(variance(desvios(notas)))