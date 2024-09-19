import cmath

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    x1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    print("\nResultados sin filtros ni alteraciones:")
    print(f"x1: {x1.real}\nx2: {x2.real}")
    
    print("\nResultados solamente con 4 decimales:")
    print(f"x1: {x1.real:.4f}\nx2: {x2.real:.4f}")
     
    print("\nResultados con los valores absolutos:")
    print(f"x1: {abs(x1.real)}\nx2: {abs(x2.real)}\n")
elif discriminante == 0:
    x = -b / (2 * a)
    print("\nLa ecuación tiene una raíz real:")
    print(f"x: {x.real}")
  
    print("\nResultados solamente con 4 decimales:")
    print(f"x: {x:.4f}")
    
    print("\nResultados con los valores absolutos:")
    print(f"x: {abs(x)}\n")
else:
    x1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    print("\nResultados sin filtros ni alteraciones:")
    print(f"x1: {x1.real}\nx2: {x2.real}")
    
    print("\nResultados solamente con 4 decimales:")
    print(f"x1: {x1.real:.4f}\nx2: {x2.real:.4f}")

    print("\nResultados con los valores absolutos:")
    print(f"x1: {abs(x1.real)}\nx2: {abs(x2.real)}\n")
