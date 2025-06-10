import matplotlib.pyplot as plt

def pedir_valores_x(): 
    while True:
        valores_x = input("Digite duas coordenadas do eixo das abscissas 'x' separando-as por espaços\n").split()
        if len(valores_x) > 2:
            print("Você digitou coordenadas a mais, digite apenas DUAS")
            continue

        if len(valores_x) > 1:
            try:
                conver_coordenadas_x = [float(valores) for valores in valores_x]
                return conver_coordenadas_x

            except ValueError:
                print("As coordenadas de x devem ser números válidos")
        
        else:
            print("Digite mais uma coordenada")
        
def pedir_valores_y(): 
    while True:
        valores_y = input("Digite as coordenadas do eixo das ordenadas 'y' separando-as por espaços\n").split()
        if len(valores_y) > 2:
            print("Você digitou coordenadas a mais, digite apenas DUAS")
            continue

        if len(valores_y) > 1:
            try:
                conver_coordenadas_y = [float(valores) for valores in valores_y]
                return conver_coordenadas_y

            except ValueError:
                print("As coordenadas de x devem ser números válidos")
        
        else:
            print("Digite mais uma coordenada")

def mostrar_valores(coordenadas_x,coordenadas_y):
    print(f"Sua reta será composta das seguintes coordenadas: X(a,b) = {coordenadas_x[0]},{coordenadas_x[1]} Y(a,b) = {coordenadas_y[0]},{coordenadas_y[1]}")

def criar_reta(coordenadas_x,coordenadas_y):
   x = coordenadas_x
   y = coordenadas_y

   plt.plot(x,y)
   plt.xlabel("Eixo X")
   plt.ylabel("Eixo Y")

   plt.title("Criando uma Reta")
   plt.show()

def main():
    while True:
        entrada = input("CRIANDO UMA RETA\nDigite:\n1 para CRIAR UMA RETA ou 0 para SAIR\n")
        if entrada == "1":
            try:
                coordenadas_x = pedir_valores_x()
                coordenadas_y = pedir_valores_y()
                mostrar_valores(coordenadas_x,coordenadas_y)
                criar_reta(coordenadas_x,coordenadas_y)
            except ValueError:
                print("Digite um caractere válido")
        elif entrada =="0":
            print("Encerrando...")
        else:
            print("Digite um caractere válido\n")
            continue
    
     
main()

    

    