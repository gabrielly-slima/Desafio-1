def calcular_media():
    notas = [float(nota) for nota in notas]
    media = sum(notas) / len(notas)
    print(f"A média do aluno {nome} é {media:.2f}")

while True:
    nome = input("Digite o nome do aluno:\n")
    notas = input("Digite as três notas do aluno, valores de 0 a 10, separando-os por espaços:\n").split()

    try:
        if not (0 <= notas <= 10):
            notas = [float(nota) for nota in notas]
            media = sum(notas) / len(notas)
            print(f"A média do aluno {nome} é {media:.2f}")
            break
        else:
            print("Você digitou um número inválido")
    except ValueError:
        print("Digite um número válido, entre 0 a 10")


            
