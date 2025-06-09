def values():
    a_value = input("Digite o valor de 'a'\n")
    operator_one = input("Digite o sinal da operação\n")
    b_value = input("Digite o valor de 'b'\n")
    operator_two = input("Digite o sinal da operação\n")
    c_value = input("Digite o valor de 'c'\n")

    return {"a":a_value,
            "op1":operator_one,
            "b":b_value,
            "op2":operator_two,
            "c":c_value}

def calculate_first_degree(data):
    print(f"Sua expressão é {data["a"]} {data["op1"]} {data["b"]} {data["op2"]} {data["c"]}")


entrada = input("CALCULO DE EQUAÇÕES\n Digite 1 se quiser calcular uma equação do PRIMEIRO GRAU\n Digite 2 se quiser calcular uma equação do SEGUNDO GRAU\n")

if entrada == "1":
    data = values()
    calculate_first_degree(data)
elif entrada =="2":
    values()



