def values(degree):
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
    print(f"Sua expressão é {data['a']} {data['b']} ")
    print(f"f(x) = {data['a']}x {data['b']}")
    result_x = data["a"]/data["b"]
    print(f"f(x)= {result_x}")

def calculate_second_degree(data):
    print(f"Sua expressão é {data['a']} {data['b']} {data['c']}")
    print(f"f(x)=")

def delta_calculate(data):
    result_delta = {data["b"]**2} - 4 * {data["a"]} * {data["c"]}
    print(result_delta)

def error_message():
    print("Caractere inválido! Insira o valor correto pedido")

def main():
    while True:
        entrada = input("CALCULO DE EQUAÇÕES\n Digite 1 se quiser calcular uma equação do PRIMEIRO GRAU\n Digite 2 se quiser calcular uma equação do SEGUNDO GRAU\n Ou digite 0 para ENCERRAR o programa\n")

        if entrada =="1":
            data = values(1)
            calculate_first_degree(data)
            break

        elif entrada =="2":
            values(2)
            delta_calculate()
            break

        elif entrada =="0":
            print("Encerrando...")
            break
        
        else:
            error_message()
            continue

        

main()


