#para trabalhar circularidade, vamos lidar com o resto do topo de uma faixa!!
#Considerando uma faixa entre 0 e 25, qdo eu faço o resto da divisão por um valor maior que essa faixa, o valor do resto volta a variar a partir de zero ao topo da faixa novamente. Assim, circulamos dentro da faixa estabelecida.
def criptografa_cesar(senha):
    for char in senha:
        if ('a' <= char <= 'z'):
            #1 etapa: converto minha letra para o asci int e substraio de 'a' 
            # para pegar posicao no alfabeto.
            pos_char_original = ord(char) - ord('a')
            #2 etapa: define a nova letra garantindo a circularidade
            pos_nova = ((pos_char_original + 3) % 26) + ord('a')
            #3 etapa: converte para char e compoe a string
            nova_senha += chr(pos_nova)
        elif ('A' <= char <= 'Z'):
            pos_char_original = ord(char) - ord('A')
            pos_nova = ((pos_char_original + 3) % 26) + ord('A')
        else:
            nova_senha += char
        
        return nova_senha