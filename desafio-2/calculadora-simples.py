def somar(numeros):
    return sum(numeros)

def subtrair(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n
    return resultado

def multiplicar(numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado

def dividir(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            print("Erro! Não é possível dividir por zero")
            return None
        resultado /= n
    return resultado

def exibir_resultado(resultado):
    if resultado is not None:
        print(f"O resultado é: {resultado}")

# Loop principal
while True:
    entrada = input("Digite os números separando-os por espaços\nPara sair digite: SAIR\n").strip().upper()

    if entrada == "SAIR":
        print("Obrigado por jogar!")
        break

    try:
        numeros = [float(n) for n in entrada.split()]
    except ValueError:
        print("Por favor, insira apenas números válidos")
        continue

    operador = input("Digite qual tipo de operação você quer realizar. Para somar: +\nPara subtrair: -\nPara multiplicar: *\nPara dividir: /\n").strip()

    if operador == "+":
        resultado = somar(numeros)
    elif operador == "-":
        resultado = subtrair(numeros)
    elif operador == "*":
        resultado = multiplicar(numeros)
    elif operador == "/":
        resultado = dividir(numeros)
    else:
        print("Digite um operador válido")
        continue

    exibir_resultado(resultado)
