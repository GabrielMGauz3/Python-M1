import math
co = float(input("Receba o valor do cateto oposto: "))
ca = float(input("Receba o valor do cateto adjacente: "))

hi = math.hypot(co, ca)
hip = co**2 + ca**2
hipotenusa = math.sqrt(hip)

print("A Hipotenusa do cateto oposto {} e Adjacente {} é {}" .format(co, ca, hi))
print("hip = {} e Hipotenusa = {}".format(hip, hipotenusa))


