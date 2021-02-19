discriminating = lambda a, b, c : int((b**2)-(4*a*c))

def formulageneral():
    if(x == 0):
        return ("x", ((-b+(((b**2)-(4*a*c))**0.5))/(2*a)))
    else:
        return ("x1", ((-b+(((b**2)-(4*a*c))**0.5))/(2*a))), ("x2", ((-b-(((b**2)-(4*a*c))**0.5))/(2*a)))

print("Bienvenido!!")
print("Script para resolver ecuaciones cuadráticas.")
print("Ax^2 + Bx + C = 0")

a = float(input("Ingrese el valor del coeficiente A: "))
while(a == 0):
    a = float(input("Este valor no puede ser 0, ingrese otro valor: "))
b = float(input("Ingrese el valor del coeficiente B: "))
c = float(input("Ingrese el valor del coeficiente C: "))

x = discriminating(a, b, c)

if(x < 0):
    print("El valor de la discriminante es", x, ",no hay solución en los reales para la ecuación mostrada")
elif(x == 0):
    print("El valor de la discriminante es", x, ",solo hay una solucion", formulageneral())
else:
    print("El valor de la discriminante es", x, "asi que hay dos soluciones", formulageneral())