from geo import Punto, Linea, Area


def main():
    p1 = Punto("P001", "Punto A", 0, 0, 0)
    p2 = Punto("P002", "Punto B", 10, 0, 0)
    p3 = Punto("P003", "Punto C", 10, 10, 0)
    p4 = Punto("P004", "Punto D", 0, 10, 0)

    linea1 = Linea("L001", "Línea AB", points=[p1, p2])
    linea2 = Linea("L002", "Línea BCDA", points=[p2, p3, p4, p1])
    print(linea1)
    print("Longitud línea1:", linea1.length())
    print(linea2)
    print("Longitud línea2:", linea2.length())
    print("¿Línea2 válida?", linea2.is_valid())

    area1 = Area("A001", "Parcela 1", points=[p1, p2, p3])
    print(area1)
    print("Área 1:", area1.area())
    print("¿Área 1 válida?", area1.is_valid())

    area2 = Area("A002", "Parcela Completa", points=[p1, p2, p3, p4])
    print(area2)
    print("Área 2:", area2.area())

    p_extra = Punto("P005", "Punto E", 5, 5)
    line = Linea("L003", "Linea con punto extra")
    line.add_point(p1)
    line.add_point(p_extra)
    line.add_point(p2)
    print(line)
    print("Longitud de L003:", line.length())

    print("\nComprobaciones de jerarquía y representación:")
    for obj in (p1, linea1, area2):
        print(obj, "->", isinstance(obj, Punto), isinstance(obj, Linea), isinstance(obj, Area))


if __name__ == "__main__":
    main()