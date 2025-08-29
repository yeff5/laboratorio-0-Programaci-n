import math
def bsa(height_cm, weight_kg):
    """
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)

def categoria_bsa(Valor):
        if Valor < 1.2:
            return 0  
        elif 1.2 <= Valor < 1.5:
            return 1
        elif 1.5 <= Valor < 1.9:
            return 2
        elif 1.9 <= Valor <= 2.2:
            return 3
        else:
            return 4

          
npersonas = int(input("Ingrese el numero de personas a las que se les calculara BSA:"))
contador = [0,0,0,0,0]
categorias = ["Muy bajo","Bajo","Normal","Alto","Muy alto"]

for i in range(npersonas):
    if __name__ == "__main__":
        print(f"\nPersona {i+1}:")
        h = float(input("Altura (cm): "))
        w = float(input("Peso (kg): "))
        area = bsa(h, w)
        categoria = categoria_bsa(area)
        contador[categoria]+=1
        print(f"Su BSA es de:{area:.2f}, {categorias[categoria]}")
        
for i in range(len(categorias)):
    calculo = (contador[i]/npersonas)*100
    print(f"\n{categorias[i]}: {contador[i]} personas ({calculo}%)")
       
        