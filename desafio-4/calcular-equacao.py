import math 

def values(degree):
    '''
    Recebe os valores de a e b (para equações do primeiro grau)
    ou a, b e c (para equações do segundo grau).
    
    Verifica se a = 0, e caso seja, imprime uma mensagem de erro
    e solicita novamente os valores.
    
    Retorna um dicionário com os coeficientes.
    '''
    while True:
        try: 
            a_value = int(input("Digite o valor de 'a'\n"))
            if a_value ==0:
                print("Erro! O valor de 'a' não pode ser zero")
                continue

            b_value = int(input("Digite o valor de 'b'\n"))

            if degree ==2:
                c_value = int(input("Digite o valor de 'c'\n"))
                return {"a":a_value,
                "b":b_value,
                "c":c_value}
            else:
                return {"a":a_value,
                "b":b_value,}
        except ValueError:
            error_message()
            continue

def calculate_first_degree(data):
    '''
    Calcula e imprime a expressão algébrica e a solução da equação do primeiro grau.

    Parâmetros:
    data (dict): Dicionário com os coeficientes 'a' e 'b' da equação f(x) = ax + b.

    A função imprime a equação formatada e o valor de f(x).
    '''
    if data["b"] > 0:
        print(f"Sua expressão é f(x) = {data['a']}x + {data['b']} ")
    else:
        print(f"Sua expressão é f(x) = {data['a']}x - {data['b']} ")
    result_x = data["a"]/data["b"]
    print(f"f(x)= {result_x}")

def calculate_second_degree(data):
    '''
    Calcula e imprime a expressão algébrica e as raízes da equação do segundo grau.

    Parâmetros:
    data (dict): Dicionário com os coeficientes 'a', 'b' e 'c' da equação f(x) = ax² + bx + c.

    A função imprime a equação formatada e as raízes reais (caso existam).
    '''
    if data["b"] and data["c"] > 0:
        print(f"Sua expressão é f(x) = {data['a']}x² + {data['b']}x + {data['c']}")
    elif data["b"] > 0:
        print(f"Sua expressão é f(x) = {data['a']}x² + {data['b']}x {data['c']}")
    elif data["c"] > 0:
        print(f"Sua expressão é f(x) = {data['a']}x² {data['b']}x + {data['c']}")
    else:
        print(f"Sua expressão é f(x) = {data['a']}x² {data['b']}x {data['c']}")
    
    delta = delta_calculate(data)
    if delta is not None:
        first_raiz = (-(data["b"]) + math.sqrt(delta_calculate(data))) / (2 * data["a"])
        second_raiz = (-(data["b"]) - math.sqrt(delta_calculate(data))) / (2 * data["a"])
        print(f"A equação teve por resultado as raízes {first_raiz} e {second_raiz}")

def delta_calculate(data):
    '''
    Calcula o delta (discriminante) da equação do segundo grau a partir dos coeficientes em data.

    Parâmetros:
    data (dict): Dicionário com os coeficientes 'a', 'b' e 'c' da equação.

    Retorna:
    float: Valor do delta.
    None: Se delta for menor que zero, indicando que não existem raízes reais.
    
    A função também imprime uma mensagem caso não existam raízes reais.
    '''
    result_delta = (data["b"]**2) - 4 * data["a"] * data["c"]
    if result_delta < 0:
        print("A equação não tem raízes reais")
        return None
    return result_delta

def error_message():
    '''
    Exibe mensagem de erro
    '''
    print("Caractere inválido! Insira o valor correto pedido")

def main():
    '''
    MENU PRINCIPAL

    Solicita a entrada ao usuário.
    1. Para cálculo de equação do primeiro grau
    2. Para cálculo de equação do segundo grau
    0. Para encerrar
    '''
    while True:
        entrada = input("CALCULO DE EQUAÇÕES\n Digite 1 se quiser calcular uma equação do PRIMEIRO GRAU\n Digite 2 se quiser calcular uma equação do SEGUNDO GRAU\n Ou digite 0 para ENCERRAR o programa\n")

        if entrada =="1":
            data = values(1)
            calculate_first_degree(data)
        elif entrada =="2":
            data = values(2)
            calculate_second_degree(data)
        elif entrada =="0":
            print("Encerrando...")
            break
        else:
            error_message()
            continue

main()


