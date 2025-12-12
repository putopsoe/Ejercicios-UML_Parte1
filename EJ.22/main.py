from ciudad import Ciudad, Calle, Plaza, Edificio, ElementoEstructural, TipoElemento
from typing import List


def main():
    ciudad = Ciudad("Ciudad Bella", "País Ejemplo")

    calle_larga = Calle("Calle Larga", longitud=1200)
    plaza_mayor = Plaza("Plaza Mayor", superficie=900)

    ciudad.add_espacio(calle_larga)
    ciudad.add_espacio(plaza_mayor)

    edificio1 = Edificio("Casa del Sol", numero="1A", plantas=3)
    edificio1.add_elemento(ElementoEstructural("E01", TipoElemento.PORTADA))
    edificio1.add_elemento(ElementoEstructural("E02", TipoElemento.VENTANA))
    edificio1.add_elemento(ElementoEstructural("E03", TipoElemento.BALCON))

    edificio2 = Edificio("Edificio Aurora", numero="10", plantas=4)
    edificio2.add_elemento(ElementoEstructural("E04", TipoElemento.PUERTA))
    edificio2.add_elemento(ElementoEstructural("E05", TipoElemento.VENTANA))
    edificio2.add_elemento(ElementoEstructural("E06", TipoElemento.VENTANA))
    edificio2.add_elemento(ElementoEstructural("E07", TipoElemento.BALCON))

    edificio3 = Edificio("Portal de la Plaza", numero="2", plantas=2)
    edificio3.add_elemento(ElementoEstructural("E08", TipoElemento.PORTADA))
    edificio3.add_elemento(ElementoEstructural("E09", TipoElemento.VENTANA))
    edificio3.add_elemento(ElementoEstructural("E10", TipoElemento.VENTANA))

    calle_larga.add_edificio(edificio1)
    calle_larga.add_edificio(edificio2)
    plaza_mayor.add_edificio(edificio3)

    print(ciudad)
    print("Número de espacios:", ciudad.contar_espacios())
    print("Número total de edificios:", ciudad.contar_edificios())

    print("\nEspacios, edificios y riqueza de fachadas:")
    for esp in ciudad.espacios:
        print(esp)
        for ed in esp.edificios:
            print(" ", ed, "-> elementos:", ed.contar_elementos_por_tipo(), "riqueza:", ed.riqueza_fachada())

    print("\nConteo global de elementos por tipo:")
    conteo = ciudad.contar_elementos_por_tipo()
    for tipo, n in conteo.items():
        print(" ", tipo.value + ":", n)

    ordenados = ciudad.edificios_ordenados_por_riqueza()
    print("\nEdificios ordenados por riqueza de fachada:")
    for ed in ordenados:
        print(" ", ed, "riqueza:", ed.riqueza_fachada())


if __name__ == "__main__":
    main()