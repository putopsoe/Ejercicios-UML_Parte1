from datetime import date, timedelta
from museo import (
    Edificio,
    Planta,
    Sala,
    Almacen,
    Coleccion,
    ColeccionTemporal,
    Objeto,
    Restauracion,
    EstadoObjeto,
    Tematica,
    Origen
)


def main():
    edificio = Edificio("Museo Nacional", "Plaza Central 1")
    p1 = Planta(numero=1)
    p2 = Planta(numero=2)
    p3 = Planta(numero=3)
    edificio.add_planta(p1)
    edificio.add_planta(p2)
    edificio.add_planta(p3)

    sala_antiguedades = Sala("S1", "Sala de Antigüedades", esta_abierta_al_publico=True)
    almacen_general = Almacen("A1", "Almacén General")
    p1.add_ubicacion(sala_antiguedades)
    p1.add_ubicacion(almacen_general)

    coleccion_permanente = Coleccion("Permanente", "Colección permanente del museo")
    coleccion_temporal = ColeccionTemporal("Temporal: Exposición Fenicios", "Exposición temporal", date.today(), date.today() + timedelta(days=30))

    obj1 = Objeto("OBJ001", "Vasija fenicia", "Autor desconocido", date(500, 1, 1), "Vasija decorativa", Origen.HALLAZGO, EstadoObjeto.BUENO, Tematica.ARQUEOLOGIA)
    obj2 = Objeto("OBJ002", "Figura de bronce", "Autor desconocido", date(300, 1, 1), "Figura humana", Origen.DONACION, EstadoObjeto.DETERIORADO, Tematica.HISTORIA)
    obj3 = Objeto("OBJ003", "Collar antiguo", "Autor desconocido", date(200, 1, 1), "Collar ceremonial", Origen.HALLAZGO, EstadoObjeto.BUENO, Tematica.ARQUEOLOGIA)

    coleccion_permanente.add_objeto(obj2)
    coleccion_temporal.add_objeto(obj1)
    coleccion_temporal.add_objeto(obj3)

    obj1.mover_a(sala_antiguedades)
    obj2.mover_a(almacen_general)
    obj3.mover_a(sala_antiguedades)

    resta1 = Restauracion(date.today(), "Limpieza y consolidación", "Técnica A")
    obj2.solicitar_restauracion(resta1)

    print(edificio)
    for p in edificio.plantas:
        print("  ", p)
        for u in p.ubicaciones:
            print("    ", u)
            for o in u.objetos:
                print("      ", o)

    print()
    print(coleccion_permanente)
    print(coleccion_temporal, "Vigente:", coleccion_temporal.vigente())

    print("\nRestauraciones:")
    print(resta1)
    resta1.finalizar()
    print("Después de finalizar:", obj2)

if __name__ == "__main__":
    main()