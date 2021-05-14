
def calcula_linhas(nome):
    f = open(f"{nome}.txt")
    numeroLinhas = len(f.readlines())
    return f"O ficheiro tem {numeroLinhas} linhas"


def calcula_caracteres(nome):
    caracteres = 0
    f = open(f"{nome}.txt")
    numeroLinhas = len(f.readlines())
    f.close()
    with open(f"{nome}.txt") as file:
        for line in file:
            caracteres += len(line)
    caracteres -= numeroLinhas - 1
    return f"O ficheiro tem {caracteres} caracteres"


def calcula_palavra_comprida(nome):
    maiorPalavra = ""
    f = open(f"{nome}.txt")
    texto = f.readlines()
    f.close()
    for linha in texto:
        list = linha.split()
        maiorPalavraAtual = max(list, key=len)
        if (len(maiorPalavraAtual) > len(maiorPalavra)):
            maiorPalavra = maiorPalavraAtual
    return f"A maior palavra do ficheiro é: {maiorPalavra}"


def calcula_ocorrencia_de_letras(nome):
    ocorrencias = {}
    f = open(f"{nome}.txt")
    texto = f.readlines()
    f.close()
    textoStr = ''.join(texto).lower()
    for letra in set(textoStr):
        if letra.isalpha():
            ocorrencias[letra] = textoStr.count(letra)
    return f"Ocorrencia de cada letra : {ocorrencias}"

