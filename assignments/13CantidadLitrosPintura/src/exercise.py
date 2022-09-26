
def main():
    area = float(input('Area a pintar en metros: '))
    rendi = float(input('Rendimiento (m2/l): '))
    lit = (area / rendi)
    print('Litros a comprar:', round(lit))

