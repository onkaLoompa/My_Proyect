from statistics import mean

a = float(input("Matemáticas: "))
b = float(input("Ciencias: "))
c = float(input("Historia: "))
d = float(input("Lengua :"))

notaMedia = mean([a, b, c, d])

print("Nota media:",notaMedia)