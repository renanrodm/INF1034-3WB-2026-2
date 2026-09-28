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
                palavra_aux += letra + ' '
            else:
                palavra_aux += palavra_oculta[2*i] + ' '

    palavra_oculta = palavra_aux
    print(palavra_oculta)
    if palavra_oculta == palavra_aleatoria:
        break

