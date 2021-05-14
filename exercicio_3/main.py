import os


def pede_pasta():
    while True:
        pathAtual = os.getcwd()
        path = input("Insira o path do ficheiro:\n")
        if os.path.exists(path):
            return path
        else:
            pathJunto = pathAtual + "\\" + path
            if os.path.exists(pathJunto):
                return pathJunto


def calcula_tamanho_pasta(path):
    tamanhoPasta = 0
    listaFicheiro = os.listdir(path)

    for ficheiro in listaFicheiro:
        if os.path.isfile(path + "\\" + ficheiro):
            f_path = os.path.join(path, ficheiro)
            tamanhoPasta += (os.path.getsize(f_path) / 1000000)
        elif os.path.isdir(path + "\\" + ficheiro):
            tamanhoPasta += calcula_tamanho_pasta(path + "\\" + ficheiro)

    return tamanhoPasta


def main():
    print(f"{(int)(calcula_tamanho_pasta(pede_pasta()))} MB")


if __name__ == "__main__":
    main()