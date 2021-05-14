import json
from exercicio_1.analisa_ficheiro.calculos import *

def pede_nome():
    ficheiroValido = False
    nome = ""
    while (not ficheiroValido):
        try:
            nome = input("Introduza o nome do ficheiro\n")
            f = open(f"{nome}.txt", "r")
            ficheiroValido = True
        except OSError:
            print("Não existe um ficheiro .txt com esse nome\n")
    gera_nome(nome)


def gera_nome(nome):
    f = open(f"{nome}.txt", "r")
    conteudo_dict = calcula_linhas(nome) + "\n"
    conteudo_dict += calcula_caracteres(nome) + "\n"
    conteudo_dict += calcula_palavra_comprida(nome) + "\n"
    conteudo_dict += calcula_ocorrencia_de_letras(nome)
    f.close()
    with open(f'{nome}.json', 'w') as json_file:
        json.dump(conteudo_dict, json_file, indent=4)
