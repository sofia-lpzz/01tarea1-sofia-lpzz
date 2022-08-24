def main():
    #escribe tu código abajo de esta línea
    birth = int(input('Dame el año de nacimiento: '))
    ahora = int(input('Dame el año actual: '))
    lustros = (ahora - birth) / 5
    print ('Los lustros que has vivido son:', lustros)



if __name__ == '__main__':
    main()
