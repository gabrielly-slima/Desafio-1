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

def calculate_first_degree():
    print(f"Sua expressão é {data["a"]["op1"]["b"]["op2"]["c"]}")


entrada = input("CALCULO DE EQUAÇÕES\n Digite 1 se quiser calcular uma equação do PRIMEIRO GRAU\n Digite 2 se quiser calcular uma equação do SEGUNDO GRAU\n")

if entrada == "1":
    data = values()
    values()
    calculate_first_degree()
elif entrada =="2":
    values()



