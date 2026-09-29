from random import choice

#1º lista de palavaras
palavras = ["banana", "maca", "laranja", "morango", "uva", "melancia", "abacaxi", "limao", "mamao", "pera"]

palavra_aleatoria = choice(palavras)

print(palavra_aleatoria)

palavra_oculta = "_" * len(palavra_aleatoria)
palavra_aux = ""

while palavra_oculta != palavra_aleatoria:
    
    letra = str(input("Digite uma letra: "))
    

    if letra in palavra_aleatoria:
       
        for i in range(len(palavra_aleatoria)):
            if palavra_aleatoria[i] == letra:
                palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i + 1:]
                #AO AVALIADOR: Foi considerando usar o slicing de string do Python para solucionar.
                #Dessa forma, eu crio uma nova string do jeito que quero sem precisar de string auxiliar.
                #Não consegui avançar com a lógica explicada em aula.
        print(palavra_oculta)

