from datetime import date
from actuacion import ActuacionArqueologica, TipoActuacion

def main():
    a1 = ActuacionArqueologica(date(2023, 5, 1), TipoActuacion.SONDEO, date(2023, 5, 10))
    a2 = ActuacionArqueologica(date(2024, 3, 15), TipoActuacion.EXCAVACION)  # en curso (sin fecha_fin)
    a3 = ActuacionArqueologica(date(2022, 7, 1), TipoActuacion.SEGUIMIENTO, date(2022, 7, 30))

    for a in (a1, a2, a3):
        print(a)
        print("  Atributos:", vars(a))
        print()

if __name__ == "__main__":
    main()