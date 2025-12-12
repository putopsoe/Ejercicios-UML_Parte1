from shapes import Point, Polygon

def main():
    # Puntos: usaremos una configuración similar al diagrama de ejemplo.
    p1 = Point(-10, 10)
    p2 = Point(10, 10)
    p3 = Point(10, -10)
    p4 = Point(30, -10)

    # Polígono 1: p1, p2, p3
    poly1 = Polygon(name="poly1")
    poly1.add_point(p1)
    poly1.add_point(p2)
    poly1.add_point(p3)

    # Polígono 2: comparte p2 y p3, y añade p4
    poly2 = Polygon(name="poly2")
    poly2.add_point(p2)
    poly2.add_point(p3)
    poly2.add_point(p4)

    # Mostrar polígonos
    print("Polígonos:")
    print(poly1)
    print(poly2)
    print()

    # Mostrar puntos y a qué polígonos pertenecen
    print("Puntos y polígonos asociados:")
    for p in (p1, p2, p3, p4):
        print(" ", p)

    # Cálculos geométricos
    print()
    print(f"{poly1.name} - ¿Válido? {poly1.is_valid()}, Área: {poly1.area()}, Perímetro: {poly1.perimeter()}")
    print(f"{poly2.name} - ¿Válido? {poly2.is_valid()}, Área: {poly2.area()}, Perímetro: {poly2.perimeter()}")

    # Ejemplo de eliminar un punto de un polígono (p2 sigue perteneciendo a poly1)
    poly2.remove_point(p2)
    print("\nDespués de eliminar p2 de poly2:")
    print(poly2)
    print("p2:", p2)

if __name__ == "__main__":
    main()