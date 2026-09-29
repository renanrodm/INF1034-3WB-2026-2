from random import randint


def usuario_adivinha():

    qtde_tentativas = 0
    numero_gerado = randint(1, 1023)
    print("[COMPUTADOR]: Número escolhido!")
    resultado = None

    while resultado != 0:
        tentativa = int(input(f'Escolha um numero entre 1 e 1023: '))
        qtde_tentativas += 1

        if numero_gerado < tentativa:
            print("-1")
        elif numero_gerado > tentativa:
            print("1")
        elif numero_gerado == tentativa:
            print("0")
            resultado = 0
    print(f'[COMPUTADOR] Numero escolhido: {numero_gerado}')
    print(f"[USUARIO] Tentativas: {qtde_tentativas}") 

def computador_adivinha(numero_escolhido):

    qtde_tentativas = 0
    numero_gerado = numero_escolhido
    resultado = None

    while resultado != 0:
        tentativa = randint(1, 1023)
        print(f'[COMPUTADOR] escolheu: {tentativa}')
        qtde_tentativas += 1

        if numero_gerado < tentativa:
            print("-1")
        elif numero_gerado > tentativa:
            print("1")
        elif numero_gerado == tentativa:
            print("0")
            resultado = 0
    print(f'[USUÁRIO] Numero escolhido:: {numero_gerado}')
    print(f"[COMPUTADOR] Tentativas: {qtde_tentativas}") 


jogar_navamente = True
while jogar_navamente: 
    player = input("Quem vai adivinhar? Usuário ou Computador ? u/c :  ")
    if player == "u":
        usuario_adivinha()
    elif player == "c":
        numero_escolhido = int((input("Qual numero o computador deve adivinhar: ")))
        computador_adivinha(numero_escolhido)

    entrada = input("\nDeseja jogar novamente? s/n: ")
    if entrada == "n":
        jogar_navamente = False
    