print("SAIBA QUAL ANO É BISSEXTO")
#Variavel de entrada do ano
ano = int(input("Insira o ano que você deseja saber ? "))
#Condicional Anos divisíveis por 4 são bissextos.
#Anos divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")