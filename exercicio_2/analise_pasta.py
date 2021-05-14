import os
import csv
from matplotlib import pyplot as plt

def pede_pasta():
    nome = input("Introduza o caminho da pasta\n")
    return nome

def faz_calculos(nome):
    listaTipoFicheiro = []
    tamanhoPasta = {}
    listaFicheiro = os.listdir(nome)
    for ficheiro in listaFicheiro:
        if len(ficheiro.split('.')) > 1:
            listaTipoFicheiro.append(f"{ficheiro.split('.')[1]}")

    for tipoFicheiro in set(listaTipoFicheiro):
        f_size = 0
        for ficheiro in listaFicheiro:
            if len(ficheiro.split('.')) > 1:
                if ficheiro.split('.')[1] == tipoFicheiro:
                    f_path = os.path.join(nome, ficheiro)
                    f_size += (os.path.getsize(f_path) / 1024)
        n_tipo = sum([1 for tipo in listaTipoFicheiro if tipoFicheiro == tipo])
        tamanhoPasta[tipoFicheiro] = [f"volume:{f_size}", f"quantidade:{n_tipo}"]
    return tamanhoPasta


def guarda_resultados(resultados, nome):
    ficheiroCsv = (nome.split('\\')[-1])
    with open(f"{ ficheiroCsv}.csv", "w", newline='') as ficheiro:
        campos = ['Extensao','Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        for tipo, calculos in resultados.items():
            writer.writerow({'Extensao': f"{tipo}",'Quantidade':calculos[1].split(':')[1], 'Tamanho[kByte]':calculos[0].split(':')[1]})



def faz_grafico_queijos(titulo, resultados):
    lista_valores = []
    for resultado in resultados.values():
        lista_valores.append(resultado[0].split(':')[1])
    plt.pie(lista_valores, labels=resultados.keys(), autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, resultados):
    lista_valores = []
    lista_chaves = []

    for item in sorted(resultados, key=resultados.get):
        lista_chaves.append(item)
        lista_valores.append(resultados.get(item)[0].split(':')[1])

    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()
