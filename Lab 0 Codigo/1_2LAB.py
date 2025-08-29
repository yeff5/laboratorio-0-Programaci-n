import math
def bsa(height_cm, weight_kg):
    """
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)

def categoria_bsa(Valor):
        if Valor < 1.2:
            return "Muy baja"
        elif 1.2 <= Valor < 1.5:
            return "Baja"
        elif 1.5 <= Valor < 1.9:
            return "Normal"
        elif 1.9 <= Valor <= 2.2:
            return "Alta"
        else:
            return "Muy alta"

if __name__ == "__main__":
    h = float(input("Altura (cm): "))
    w = float(input("Peso (kg): "))
    area = bsa(h, w)
    categoria = categoria_bsa(area)
    print(f"BSA estimada: {area:.2f} m² su indice es{categoria}")
   

        