from iglesia import (
    Iglesia,
    IglesiaRural,
    IglesiaMonacal,
    Nave,
    Abside,
    VentanaSimple,
    VentanaCompleja,
    FormaAbside,
    TecnicaCierreSimple,
    TecnicaCierreComplejo,
    TipoCrucero,
    Crucero
)
from datetime import date

def main():
    rural = IglesiaRural("Iglesia de San Pedro", direccion="C/ Antigua 5")
    rural.naves[0].superficie = 120.0
    abs_r = rural.absides[0]
    abs_r.add_ventana(VentanaSimple("Ventana abside", 0.8, 1.2, True, False, TecnicaCierreSimple.TELA_ENCERADA))
    print("Iglesia rural:", rural)
    print(" Detalles abside:", abs_r)
    print()

    monacal = IglesiaMonacal("Monasterio de Santa María", orden="Orden Benedictina")
    monacal.add_nave(Nave(250.0))
    monacal.add_nave(Nave(240.0))
    monacal.add_abside(Abside(FormaAbside.SEMICIRCULAR))
    monacal.add_abside(Abside(FormaAbside.SEMICIRCULAR))
    monacal.add_abside(Abside(FormaAbside.SEMICIRCULAR))
    monacal.set_crucero(Crucero(TipoCrucero.CON_BRAZOS_SALIENTES))

    for a in monacal.absides:
        a.add_ventana(VentanaSimple("Ventana abside 1", 1.0, 1.4, True, True, TecnicaCierreSimple.TELA_IMPREGNADA))
        a.add_ventana(VentanaSimple("Ventana abside 2", 1.0, 1.4, False, False, TecnicaCierreSimple.TELA_IMPREGNADA))
        a.add_ventana(VentanaCompleja("Vidriera central", 1.5, 2.0, TecnicaCierreComplejo.VIDRIERA_COLOR))

    # Añadir una ventana al conjunto de la iglesia (por ejemplo en la nave principal)
    monacal.add_ventana(VentanaCompleja("Vidriera nave central", 2.0, 3.0, TecnicaCierreComplejo.VIDRIERA_INCOLORA))

    print("Iglesia monacal:", monacal)
    print(" Naves:", monacal.naves)
    print(" Absides y ventanas por abside:")
    for a in monacal.absides:
        print("  ", a, "Ventanas:", a.ventanas)
    print(" Crucero:", monacal.crucero)
    print()

    print("Comprobaciones de validez:")
    print(" Rural es válida?:", rural.is_valid())
    print(" Monacal es válida?:", monacal.is_valid())

if __name__ == "__main__":
    main()