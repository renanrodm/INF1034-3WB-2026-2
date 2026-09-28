from random import choice

#1º lista de palavaras
palavras = ["banana", "maca", "laranja", "morango", "uva", "melancia", "abacaxi", "limao", "mamao", "pera"]

palavra_aleatoria = choice(palavras)

print(palavra_aleatoria)

palavra_oculta = "_ " * len(palavra_aleatoria)
palavra_aux = ""

while True:
    
    letra = str(input("Digite uma letra: "))
    

    if letra in palavra_aleatoria:
       
        for i in range(len(palavra_aleatoria)):
            if letra == palavra_aleatoria[i]:
                #TESTAR FATIAMENTO COM SLICING
                palavra_aux = palavra_oculta[:i] + letra + palavra_oculta[i + 1:]
                print(f"ESTADO ATUAL PALAVRA AUXILIAR: {palavra_aux}")

    palavra_oculta = palavra_aux
    print(palavra_aux)


    if palavra_oculta == palavra_aleatoria:
        break

