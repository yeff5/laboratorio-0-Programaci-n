import math
def rangoN(altura):
    bsa_min = 1.5
    bsa_max = 1.9
    peso_min = (bsa_min**2 * 3600) / altura 
    peso_max = (bsa_max**2 * 3600) / altura
    return peso_min,peso_max
        
if __name__ == "__main__":
        h = float(input("Altura (cm): "))
        rango_normal = rangoN(h)
        print(f"para su altura su peso para un BSA normal es: {rango_normal}")
        