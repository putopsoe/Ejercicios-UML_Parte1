from shapes import (
    Forma,
    Cuadrilatero,
    Rectangulo,
    Cuadrado,
    Conica,
    Circulo,
    Elipse
)


def main():
    f = Forma(color="blanco")
    cdr = Cuadrilatero(longitud=12, color="gris")
    r = Rectangulo(longitud=6, anchura=3, color="amarillo")
    cu = Cuadrado(longitud=5, color="verde")
    circ = Circulo(diametro=10, color="azul")
    el = Elipse(eje_mayor=12, eje_menor=8, color="rojo")

    objetos = (f, cdr, r, cu, circ, el)

    for obj in objetos:
        print(obj)
        if isinstance(obj, Rectangulo):
            print("  Area:", obj.area(), "Perímetro:", obj.perimetro())
        if isinstance(obj, Cuadrado):
            print("  Area:", obj.area(), "Perímetro:", obj.perimetro())
        if isinstance(obj, Circulo):
            print("  Area:", f"{obj.area():.3f}", "Perímetro:", f"{obj.perimetro():.3f}")
        if isinstance(obj, Elipse):
            print("  Area:", f"{obj.area():.3f}", "Perímetro aproximado:", f"{obj.perimetro():.3f}")
        print()

    print("Comprobaciones de jerarquía:")
    print(" - 'cu' es Cuadrado y Cuadrilatero y Forma:",
          isinstance(cu, Cuadrado), isinstance(cu, Cuadrilatero), isinstance(cu, Forma))
    print(" - 'r' es Rectangulo y Cuadrilatero y Forma:",
          isinstance(r, Rectangulo), isinstance(r, Cuadrilatero), isinstance(r, Forma))
    print(" - 'circ' es Circulo y Conica y Forma:",
          isinstance(circ, Circulo), isinstance(circ, Conica), isinstance(circ, Forma))
    print(" - 'el' es Elipse y Conica y Forma:",
          isinstance(el, Elipse), isinstance(el, Conica), isinstance(el, Forma))


if __name__ == "__main__":
    main()