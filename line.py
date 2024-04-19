def line():
    print("TO DO")
    coeficiente_A = float(input("Ingrese el coeficiente A: "))
coeficiente_B = float(input("Ingrese el coeficiente B: "))
coeficiente_X1 = float(input("Ingrese el coeficiente X1: "))
coeficiente_X2 = float(input("Ingrese el coeficiente X2: "))

print(f"El coeficiente A de su ecuación de la recta es: {coeficiente_A}")
print(f"El coeficiente B de su ecuación de la recta es: {coeficiente_B}")
print(f"El coeficiente X1 de su ecuación de la recta es: {coeficiente_X1}")
print(f"El coeficiente X2 de su ecuación de la recta es: {coeficiente_X2}")

print("Para la siguiente ecuación:")
print(f"Y = {coeficiente_A}X + {coeficiente_B}")

print("Dados los siguientes puntos:")
print(f"P1 ({coeficiente_X1}, {coeficiente_A * coeficiente_X1 + coeficiente_B})")
print(f"P2 ({coeficiente_X2}, {coeficiente_A * coeficiente_X2 + coeficiente_B})")

coeficiente_Y1 = coeficiente_A * coeficiente_X1 + coeficiente_B
coeficiente_Y2 = coeficiente_A * coeficiente_X2 + coeficiente_B

distancia = math.sqrt((coeficiente_X2 - coeficiente_X1)**2 + (coeficiente_Y2 - coeficiente_Y1)**2)
print(f"La distancia entre ellos es: {distancia}")

