def values(degree):
    while True:
        try: 
            a_value = int(input("Digite o valor de 'a'\n"))
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

def error_message():
    print("Caractere inválido! Insira o valor correto pedido")

def main():
    while True:
        entrada = input("CALCULO DE EQUAÇÕES\n Digite 1 se quiser calcular uma equação do PRIMEIRO GRAU\n Digite 2 se quiser calcular uma equação do SEGUNDO GRAU\n Ou digite 0 para ENCERRAR o programa")

        if entrada =="1":
            data = values(1)
            calculate_first_degree(data)
            break

        elif entrada =="2":
            values(2)
            break

        elif entrada =="0":
            print("Encerrando...")
            break
        
        else:
            error_message()
            continue

        

main()


