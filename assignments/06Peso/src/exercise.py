def main():
    #escribe tu código abajo de esta línea
    peso = int(input("Dame el peso inicial: "))
    final = int(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    resultado = (peso - final) / meses
    print("Lo que debes bajar por mes es:" , resultado)

if __name__ == '__main__':
    main()
