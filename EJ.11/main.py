from datetime import date
from enums import Tecnica, SubTecnica, Material, EstadoConservacion
from modelo import Cuadro, Lugar

def main():
    # Original (La Gioconda)
    louvre = Lugar(institucion="Museo del Louvre", ciudad="París", pais="Francia", titulo_lugar="Salle des États")
    gioconda = Cuadro(
        titulos=["La Gioconda", "Mona Lisa"],
        cronologia=date(1503,1,1),
        tecnica=Tecnica.OLEO,
        sub_tecnica=SubTecnica.SFUMATO,
        material=Material.ALAMO,
        autor="Leonardo da Vinci",
        estado_conservacion=EstadoConservacion.REGULAR,
        ubicacion=louvre
    )

    # Réplica (El Prado)
    prado = Lugar(institucion="Museo del Prado", ciudad="Madrid", pais="España", titulo_lugar=None)
    replica_prado = Cuadro(
        titulos=["Gioconda de El Prado"],
        cronologia=date(1503,1,1),
        tecnica=Tecnica.OLEO,
        sub_tecnica=SubTecnica.PINCELADA_SIMPLE,
        material=Material.NOGAL,
        autor="Anónimo",
        estado_conservacion=EstadoConservacion.BUENO,
        ubicacion=prado,
        replica_of=gioconda
    )

    # Mostrar resultados
    for obj in (gioconda, replica_prado, louvre, prado):
        print(obj)
        print()

if __name__ == "__main__":
    main()