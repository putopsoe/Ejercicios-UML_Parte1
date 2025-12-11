from shapes import Polygon
from shapes import Point

def main():
    # Creamos el polígono (cuadrado del enunciado)
    poly = Polygon(name="pol1")

    pt1 = Point(-10, 10)
    pt2 = Point(10, 10)
    pt3 = Point(-10, -10)
    pt4 = Point(10, -10)

    # Añadir puntos (orden cualquiera pero consistente)
    poly.add_point(pt1)
    poly.add_point(pt2)
    poly.add_point(pt4)
    poly.add_point(pt3)

    print(poly)
    print("Puntos individuales:")
    for p in (pt1, pt2, pt3, pt4):
        print(" ", p)

    print(f"\n¿Válido? {poly.is_valid()}")
    print(f"Área: {poly.area()}")
    print(f"Perímetro: {poly.perimeter()}")

    # Comprobación: intentar reasignar un punto a otro polígono debe fallar
    other = Polygon(name="other")
    try:
        other.add_point(pt1)  # pt1 ya pertenece a 'poly'
    except ValueError as e:
        print("\nComprobación de pertenencia única:", e)

if __name__ == "__main__":
    main()