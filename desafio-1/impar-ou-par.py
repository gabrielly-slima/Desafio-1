def eh_par (numero):
    return numero % 2 ==0 

print("SEJA BEM-VINDO AO JOGO DO ÍMPAR OU PAR")

while True:
    entrada = input("Digite um número qualquer ou se quiser sair digite: SAIR").strip().upper()
    
    if entrada != "SAIR":
        try:
            numero = int(entrada)
        except ValueError:
            print("\nDigite corretamente o que foi solicitado\n")
            continue

        if eh_par(numero):
            print("\nO número que você escolheu é par!\n")
            
        else:
            print("\nO número que você escolheu é ímpar!\n")

    else:
        print("Obrigado por jogar!")
        break





