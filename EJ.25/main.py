from libro import Libro, Muestra, FormaImpresion, TecnicaEncuadernacion

def main():
    l1 = Libro(180, FormaImpresion.IMPRESO, TecnicaEncuadernacion.COSIDO, identificador="LB-001")
    l2 = Libro(42, FormaImpresion.MANUSCRITO, TecnicaEncuadernacion.ENCUADERNADO)

    m1 = Muestra(0.10, "muestreo aleatorio", identificador="M-01")
    m2 = Muestra(0.50, "selección representativa")

    print("Libros:")
    print(" ", l1)
    print(" ", l2)

    print("\nMuestras:")
    print(" ", m1, "-> porcentaje:", f"{m1.porcentaje():.1f}%")
    print(" ", m2, "-> porcentaje:", f"{m2.porcentaje():.1f}%")

    try:
        Muestra(1.5, "incorrecto")
    except Exception as ex:
        print("\nEjemplo de validación: fracción inválida ->", ex)

if __name__ == "__main__":
    main()