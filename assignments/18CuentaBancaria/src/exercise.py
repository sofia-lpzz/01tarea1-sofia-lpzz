def main():
    #escribe tu código abajo de esta línea
    saldoi = float(input("Dame el saldo del mes anterior: "))
    ingreso = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldom = float(saldoi + ingreso - egresos - (cheques * 13))
    intereses = float(saldom * 0.075)
    calculo = float(saldom - intereses)
    final = print("El saldo final de la cuenta es:", calculo)



if __name__ == '__main__':
    main()
