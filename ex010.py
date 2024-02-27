altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

area_parede = altura * largura

quantidade_tinta = area_parede / 2

print("A área da parede é:", area_parede, "metros quadrados")
print("Serão necessários", quantidade_tinta, "litros de tinta para pintar a parede")
