from random import randint
import os

qtde_tentativas = 0
numero_gerado = randint(1, 1023)
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
print(f'Numero escolhido: {numero_gerado}')
print(f"Tentativas: {qtde_tentativas}") 

