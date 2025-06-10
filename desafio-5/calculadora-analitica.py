import matplotlib.pyplot as plt

def pedir_valores_x(): 
    while True:
        valores_x = input("Digite duas coordenadas do eixo das abscissas 'x' separando-as por espaços\n").split()
        if len(valores_x) > 1:
            try:
                conver_coordenadas_x = [float(valores) for valores in valores_x]
                return conver_coordenadas_x

            except ValueError:
                print("As coordenadas de x devem ser números válidos")
        elif len(valores_x) > 2:
            print("Você digitou coordenadas a mais, digite apenas duas")
            continue
        else:
            print("Digite mais uma coordenada")
        

def pedir_valores_y(): 
    while True:
        valores_y = input("Digite as coordenadas do eixo das ordenadas 'y' separando-as por espaços\n").split()
        if len(valores_y) > 1:
            try:
                conver_coordenadas_y = [float(valores) for valores in valores_y]
                return conver_coordenadas_y

            except ValueError:
                print("As coordenadas de x devem ser números válidos")
        else:
            print("Digite pelo menos mais de uma coordenada")


    


def main():
    entrada = input("CALCULADORA DE GEOMETRIA ANALÍTICA\nDigite:\n1 para calcular a EQUAÇÃO GERAL DA RETA\n2 para calcular a EQUAÇÃO FUNDAMENTAL DA RETA\n3 para calcular a EQUAÇÃO REDUZIDA DA RETA")
    if entrada == "1":
        try:
            coordenadas_x = pedir_valores_x()
            coordenadas_y = pedir_valores_y()
            mostrar_valores(coordenadas_x,coordenadas_y)
        except ValueError:
            print("deu bosta")
  
         
main()

    

    