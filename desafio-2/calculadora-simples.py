entrada = input("Digite os números separando-os por espaços\n Para sair digite: sair").strip().upper()

try:
    numeros = [float(n) for n in entrada.split()]
except ValueError:
    print("Por favor, insira apenas números válidos")

operador = input("Digite qual tipo de operação você quer realizar. Para somar: +\n Para subtrair: -\n Para multiplicar:*\n Para dividir:/\n").strip()

def somar(numeros):
   return sum(numeros)
        
def subtrair(numeros):
    resultado = numeros[0]
    for n in numeros [1:]:
        resultado -= n
    return resultado

def multiplicar(numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado

def dividir(numeros):
    resultado = numeros[0]
    for n in numeros [1:]:
        if n == 0:
            print("Erro! Não é possível dividir por zero")
            return None
        resultado /= n
    return resultado

def exibir_resultado(resultado):
    if resultado is not None:
        print(f"O resultado é: {resultado}")

if operador == "+":
    resultado = somar(numeros)
    exibir_resultado(resultado)

elif operador == "-":
    resultado = subtrair(numeros)
    exibir_resultado(resultado)

elif operador == "*":
    resultado = multiplicar(numeros)
    exibir_resultado(resultado)

elif operador == "/":
    resultado = dividir(numeros)
    exibir_resultado(resultado)

else:
    print("Digite um operador válido")