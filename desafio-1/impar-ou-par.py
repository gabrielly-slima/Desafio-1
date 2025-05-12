def verificacao (numero):
    return numero % 2 ==0 

while True:
    entrada = input("Seja bem-vindo ao jogo do ímpar ou par - Digite um número qualquer ou se quiser sair digite: SAIR")
    print(" ")
    
    if entrada != "SAIR":
        try:
            numero = int(entrada)
        except ValueError:
            print("Digite corretamente o que foi solicitado")
            continue

        if verificacao(numero):
            print("O número que você escolheu é par!")
            print(" ")
        else:
            print("O número que você escolheu é ímpar!")
            print(" ")
    else:
        print("Obrigado por jogar!")
        break





