import math
def main( variable1=x1, variable2=y1, variable3=x1, variable4=y2, x1=variable1):
    #escribe tu código abajo de esta línea
    variable1 = int(input("variable1: "))
    variable2 = int(input("Variable2: "))
    variable3 = int(input("variable3: "))
    variable4 = int(input("variable4: "))
    dist = (math.sqrt(variable3-variable1)**2+(variable4-variable2)**2)
    dist = round(dist, 2)
    print("dist:", dist)

if __name__ == '__main__':
    main()
