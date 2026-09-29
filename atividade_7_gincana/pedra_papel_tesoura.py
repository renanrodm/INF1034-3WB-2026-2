from random import choice

opcoes = ["pedra", "papel", "tesoura"]

pontuacao_jogador = 0
pontuacao_computador = 0

while True:
    print("\n===== PEDRA, PAPEL E TESOURA =====")
    print("Pontuação:")
    print(f"Jogador: {pontuacao_jogador}")
    print(f"Computador: {pontuacao_computador}")

    jogador = input("\nEscolha pedra, papel ou tesoura: ")
    
    if jogador not in opcoes:
        print("Opção inválida!")
        continue

    computador = choice(opcoes)

    print(f"Você jogou: {jogador}")
    print(f"O computador jogou: {computador}")

    if jogador == computador:
        print("Empate!")

    elif jogador == "pedra" and computador == "tesoura":
        print("Você venceu!")
        pontuacao_jogador += 1
    elif jogador == "papel" and computador == "pedra":
        print("Você venceu!")
        pontuacao_jogador += 1
    elif jogador == "tesoura" and computador == "papel":
        print("Você venceu!")
        pontuacao_jogador += 1
    else:
        print("O computador venceu!")
        pontuacao_computador += 1

    continuar = input("\nDeseja jogar novamente? (s/n): ")

    if continuar != "s":
        break

print("\n===== FIM DE JOGO =====")
print(f"Pontuação final do jogador: {pontuacao_jogador}")
print(f"Pontuação final do computador: {pontuacao_computador}")