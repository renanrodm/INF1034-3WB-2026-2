def valida_email(email):
    return email[-8:] == "@puc.com"

def verifica_maiscula(palavra):
    for l in palavra:
        if 'A' <= l <= 'Z':
            return True
    return False
        
def verifica_minuscula(palavra):
    for l in palavra:
        if 'a' <= l <= 'z':
            return True
    return False

def verifica_num(palavra): 
    for l in palavra:
        if '0' <= l <= '9':
            return True
    return False


def valida_senha(senha: str):
    possui8Chars = len(senha) >= 8
    possuiMaiscula = verifica_maiscula(senha)
    possuiMinuscula = verifica_minuscula(senha)
    possuiNum = verifica_num(senha)

    return possui8Chars and possuiMaiscula and possuiMinuscula and possuiNum
