class automovel:
    def __init__(self,capacidade,quantidade,consumo):
        self.cap_dep = capacidade
        self.quant_comb = quantidade
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return int((self.quant_comb / self.consumo) * 100)

    def abastece(self, n_litros):
        if (n_litros + self.quant_comb ) < self.cap_dep:
            self.quant_comb = n_litros + self.quant_comb
            return self.autonomia()
        else:
            print("Erro: Excedeu capacidade de combustivel")

    def percorre(self,n_km):
        if self.autonomia() > n_km:
            self.quant_comb-= (n_km * self.consumo)/100
            return self.autonomia()
        else:
            return -1

def main():
    a1 = automovel(0,0,0)
    sair = True
    while sair:
        print("0 - Defenir Parametros do Carro\n1 - Combustivel no Depósito\n2 - Autonomia Restante\n3 - Abastecer Depósito"
              "\n4 - Percorrer um trajeto\n5- Sair")
        opcao = input("Introduza uma opção:\n")
        if(opcao) == "0":
            a1.cap_dep = int(input("Defina a capacidade do depósito:\n"))
            a1.quant_comb = int(input("Defina a quantidade de combustivel no depósito:\n"))
            a1.consumo = int(input("Defina o consumo do automóvel (1litro por 100km):\n"))
        elif (opcao) == "1":
            print(a1.combustivel())
        elif (opcao) == "2":
            print(a1.autonomia())
        elif (opcao) == "3":
            a1.abastece(int(input("Defina uma quantidade em litros para abastecer:\n")))
        elif (opcao) == "4":
            a1.percorre(int(input("Introduza uma distancia em km para percorrer:\n")))
        elif (opcao) == "5":
            sair = False
        print("\n")

if __name__ == "__main__":
    main()

