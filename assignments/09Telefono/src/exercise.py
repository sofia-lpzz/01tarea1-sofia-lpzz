def main():
    mensajes = int(input('Dame el número de mensajes: '))
    megas= float(input('Dame el número de megas: '))
    minutos = int(input('Dame el número de minutos: '))
    precio = (mensajes + megas+ minutos) * 0.80
    print('El costo mensual es:', precio)




if __name__ == '__main__':
    main()
