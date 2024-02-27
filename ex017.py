import math
ang_graus = float(input("Digite um ângulo em graus: "))
ang_radianos = math.radians(ang_graus)

seno = math.sin(ang_radianos)
cosseno = math.cos(ang_radianos)
tangente = math.tan(ang_radianos)

print("SENO {} / COSSENO {} / TANGENTE {}".format(seno, cosseno, tangente))
