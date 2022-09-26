def main():
    #escribe tu código abajo de esta línea
    New = int(input('Dame la cantidad de juegos nuevos: '))
    Old = int(input('Dame la cantidad de juegos usados: '))
    pago = (New * 1000) + (Old * 350)
    print('El total de la compra es:', pago)





if __name__ == '__main__':
    main()
