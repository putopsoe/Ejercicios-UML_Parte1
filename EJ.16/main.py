from datetime import date
from persona import Persona

def main():
    carlos = Persona("Carlos", "González", date(1960, 7, 14), "Hombre")
    diana = Persona("Diana", "López", date(1965, 5, 20), "Mujer")
    guillermo = Persona("Guillermo", "González", date(1988, 6, 21), "Hombre")
    kate = Persona("Kate", "Martínez", date(1990, 8, 2), "Mujer")
    ben = Persona("Ben", "González", date(2015, 3, 10), "Hombre")

    guillermo.casar_con(kate)
    guillermo.establecer_padres(carlos, diana)
    carlos.anadir_hijo(guillermo)
    diana.anadir_hijo(guillermo)
    guillermo.anadir_hijo(ben)
    kate.anadir_hijo(ben)

    print("Personas:")
    for p in (carlos, diana, guillermo, kate, ben):
        print(p)
    print()

    print("Relaciones comprobadas:")
    print(f"{guillermo.nombre_completo()} tiene cónyuge: {guillermo.conyuge.nombre_completo()}")
    print(f"{guillermo.nombre_completo()} tiene padre: {guillermo.padre.nombre_completo()}, madre: {guillermo.madre.nombre_completo()}")
    print(f"{ben.nombre_completo()} es hijo de: {ben.padre.nombre_completo()} y {ben.madre.nombre_completo()}")

    guillermo.casar_con(None)
    print()
    print("Después del divorcio de Guillermo:")
    print(guillermo)
    print(kate)

if __name__ == "__main__":
    main()