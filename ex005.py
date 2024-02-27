import math

n = int(input("Digite um numero para saber seu dobro, seu triplo e a raiz quadrada: "))
dobro = n*2
triplo = n*3
raiz = n**0.5
#n**(1/2) pow(n, (1/2)) pode ser usado tudo dentro no format) beneficios economia de alocaçao de memória
#desvantagem caso necessite novamente da mesma informação nao estará alocado na mémoria
raizq = math.sqrt(n)

print("dobro é {}, o triplo é {} e a raiz quadra é {:.3f} comparando {:.3f}" .format(dobro, triplo, raiz, raizq))

