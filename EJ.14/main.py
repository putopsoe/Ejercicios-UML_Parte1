from shapes_shared import PointShared, Triangle

def main():
    # Creamos puntos (dos triángulos que comparten la arista p2-p3)
    p1 = PointShared(-10, 10)
    p2 = PointShared(10, 10)
    p3 = PointShared(10, -10)
    p4 = PointShared(30, -10)  # vértice externo del segundo triángulo

    # Triángulo t1: p1, p2, p3
    t1 = Triangle(name="t1")
    t1.add_point(p1)
    t1.add_point(p2)
    t1.add_point(p3)

    # Triángulo t2: comparte la arista p2-p3, y añade p4
    t2 = Triangle(name="t2")
    t2.add_point(p2)  # punto compartido
    t2.add_point(p3)  # punto compartido
    t2.add_point(p4)

    # Mostrar triángulos
    print("Triángulos:")
    print(t1)
    print(t2)
    print()

    # Mostrar puntos y en qué triángulos participan
    print("Puntos y triángulos asociados:")
    for p in (p1, p2, p3, p4):
        print(" ", p)

    # Cálculos geométricos
    print()
    print(f"{t1.name} - Área: {t1.area()}, Perímetro: {t1.perimeter()}")
    print(f"{t2.name} - Área: {t2.area()}, Perímetro: {t2.perimeter()}")

if __name__ == '__main__':
    main()