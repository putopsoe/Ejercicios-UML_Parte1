from datetime import date
from edificio import Edificio, Hospital, Escuela, Vivienda
from datetime import timedelta

def main():
    edificio = Edificio("Edificio Central", "C/ Principal 10")

    uso_hospital_1 = Hospital(fecha_inicio=date(2000, 1, 1), fecha_fin=date(2010, 12, 31), camas=120)
    uso_escuela_1 = Escuela(fecha_inicio=date(2011, 1, 1), fecha_fin=date(2018, 6, 30), plazas=500)
    uso_vivienda_parcial = Vivienda(fecha_inicio=date(2017, 1, 1), fecha_fin=date(2019, 12, 31), unidades=10)
    uso_escuela_actual = Escuela(fecha_inicio=date(2019, 7, 1), plazas=450)
    uso_vivienda_actual = Vivienda(fecha_inicio=date(2020, 1, 1), unidades=6)

    edificio.add_uso(uso_hospital_1)
    edificio.add_uso(uso_escuela_1)
    edificio.add_uso(uso_vivienda_parcial)
    edificio.add_uso(uso_escuela_actual)
    edificio.add_uso(uso_vivienda_actual)

    print(edificio)
    print("Usos (todos):")
    for u in edificio.usos:
        print(" ", u)

    hoy = date.today()
    print(f"\nUsos actuales (hoy={hoy.isoformat()}):")
    for u in edificio.usos_actuales(hoy):
        print(" ", u)

    print("\nHistórico:")
    for u in edificio.usos_historicos(hoy):
        print(" ", u)

    print("\nCerrar la escuela actual (fecha hoy):")
    edificio.cerrar_uso(uso_escuela_actual, hoy)
    for u in edificio.usos_actuales(hoy):
        print(" ", u)

    print("\nReemplazar uso vivienda parcial por uno nuevo que comienza hoy:")
    nueva_vivienda = Vivienda(fecha_inicio=hoy, unidades=8)
    edificio.reemplazar_uso(uso_vivienda_parcial, nueva_vivienda)
    for u in edificio.usos:
        print(" ", u)

if __name__ == "__main__":
    main()