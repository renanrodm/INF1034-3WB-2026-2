# PRINCIPAL (300XP)
# - Único que não é jogo, porém tem que funcionar como uma calculadora vagabunda (100XP);
# - Portanto, ela deve ter uma memória da ÚLTIMA OPERAÇÃO FEITA (100XP);
# - Exemplo: Se eu digito 5, depois X, depois 3, o resultado que aparece é 15;
# - Se eu quiser usar esse 15, eu consigo, é só eu digitar +, e depois 4, para obter 19;
# - Não operar com mais de dois operandos (100XP);

operadores = ["+", "-", "x", "/"]
ultima_operacao = None
sair = False

while sair != True:
    resultado = 0
    if ultima_operacao == None:
    
        primeiro_operando = float(input("Entre com o primeiro operando: "))
        operacao = input("Selecione a operação? [ + ] [ - ] [ x ] [ / ] : ")
        
    else:
        print(f'Ultima operação: {ultima_operacao}')
        primeiro_operando = ultima_operacao
        operacao = input("Selecione a operação? [ + ] [ - ] [ x ] [ / ] : ")

    if operacao not in operadores:
                print("Operador incorreto")
                continue

    segundo_operando = float(input("Entre com o segundo operando: "))

    if operacao == "+":
        resultado = primeiro_operando + segundo_operando
    elif operacao == "-":
        resultado = primeiro_operando - segundo_operando
    elif operacao == "x":
        resultado = primeiro_operando * segundo_operando
    elif operacao == "/":
        if segundo_operando == 0:
            print("Não é possível dividir por zero.")
            continue
        else:
            resultado = primeiro_operando / segundo_operando

    ultima_operacao = resultado

    print(f'{primeiro_operando} {operacao} {segundo_operando} = {resultado}')

    opcao_usuario = input("Deseseja sair? [sim/nao]: ")
    if opcao_usuario == "sim":
        sair = True
    


