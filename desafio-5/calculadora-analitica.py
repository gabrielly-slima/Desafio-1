import matplotlib.pyplot as plt
entrada = input("CALCULADORA DE GEOMETRIA ANALÍTICA\nDigite:\n1 para calcular a EQUAÇÃO GERAL DA RETA\n2 para calcular a EQUAÇÃO FUNDAMENTAL DA RETA\n3 para calcular a EQUAÇÃO REDUZIDA DA RETA")
    if entrada == "1":
        try:
            main()
        except ValueError:
            print("bosta")
        
def main(): 
    while True:
        valores_x = input("Digite as coordenadas do eixo das abscissas 'x' separando-as por espaços\n").split()
        if len(valores_x) > 1:
            try:
                conver_coordenadas_x = [float(valores) for valores in valores_x]
                print(conver_coordenadas_x)
                break

            except ValueError:
                print("As coordenadas de x devem ser números válidos")
        else:
            print("Digite pelo menos mais de uma coordenada")

         


    

    