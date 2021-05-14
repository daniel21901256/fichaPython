import analise_pasta


def main():
    nome = analise_pasta.pede_pasta()
    resultados = analise_pasta.faz_calculos(nome)
    analise_pasta.guarda_resultados(resultados, nome)
    analise_pasta.faz_grafico_queijos("TamanhoDeFicheiros",resultados)
    analise_pasta.faz_grafico_barras("TamanhoDeFicheiros",resultados)


if __name__ == "__main__":
    main()
