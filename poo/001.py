class Televisao():
    def __init__(self, marca, ano, preco, n_canais):
        print(f"O objeto  {self} foi construido")
        self.ano = ano
        self.marca = marca
        self.n_canais = n_canais
        self.preco = preco

    def aumentar_canais(self):
        self.n_canais += 1


tv1 = Televisao('samsung', 2011, 1000, 10)

print(tv1.n_canais)
tv1.aumentar_canais()
print(tv1.n_canais)

for i in range(5):
    tv1.aumentar_canais()

print(tv1.n_canais)
