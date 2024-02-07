def Fahrenheit(F):
    C = (5/9) * (F - 32)
    return C
    
F = float(input())
C = Fahrenheit(F)
print(f"{F} F = {C:.2f} C.")