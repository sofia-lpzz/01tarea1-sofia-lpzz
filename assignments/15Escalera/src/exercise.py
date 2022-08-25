import math
def main():
    #escribe tu código abajo de esta línea
    alt = int(input("Altura de la casa: "))
    ang = float(input("Angulo en grados: "))
    ang = float(math.sin(math.radians(ang)))
    large = round(alt/ang)
    print("Largo de la escalera:" , large)

if __name__ == '__main__':
    main()
