#Condições Aninhadas
#APROVAÇÂO DE EMPRESTIMO
#Variaveis de entrada de informações
valor_casa = float(input("Qual é o valor do imovel desejado: "))
salario = float(input("Quanto você ganha por mês: "))
anos = int(input("Em quantos anos você deseja pagar: "))

prazo = anos * 12
prestacao = valor_casa / prazo

#Condicional é caso exceda 30% do valor do salario o financiamento seja recusado

if prestacao > salario * 30 / 100:
    print("Infelizmente o imovel excede 30% do valor do seu sálario! Financiamento \033[2;30;41mNÂO APROVADO\033[m !")
    print("Prazo {} meses // Valor da parcela {:.2f}".format(prazo, prestacao))
else:
    print("Parabéns, seu financiamento foi \033[2;30;42mAPROVADO\033[m")
    print("Seu prazo é de {} meses com o valor da parcela em {:.2f}".format(prazo, prestacao))



