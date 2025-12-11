from datetime import date
from proyecto import Proyecto
from miembro_equipo import MiembroEquipo
from lugar_actuacion import LugarActuacion

def main():
    # Crear miembros del equipo
    ana = MiembroEquipo("Ana", "García López", roles=["Jefe de Proyecto"])
    carlos = MiembroEquipo("Carlos", "Martínez Pérez", roles=["Desarrollador", "Tester"])
    maria = MiembroEquipo("María", "Rodríguez Silva", roles=["Desarrolladora", "Analista"])
    juan = MiembroEquipo("Juan", "López Fernández", roles=["Diseñador"])

    # Crear lugares de actuación
    madrid = LugarActuacion(40.4168, -3.7038, nombres=["Oficina Madrid", "Sede Principal"])
    barcelona = LugarActuacion(41.3851, 2.1734, nombres=["Oficina Barcelona"])
    remoto = LugarActuacion(0.0, 0.0, nombres=["Trabajo Remoto"])

    # Crear proyectos
    proyecto1 = Proyecto(
        nombre="Sistema de Gestión",
        fecha_inicio=date(2024, 1, 15),
        fecha_fin=date(2025, 6, 30)
    )

    proyecto2 = Proyecto(
        nombre="Portal Web",
        fecha_inicio=date(2024, 6, 1),
        fecha_fin=date(2025, 12, 31)
    )

    # Establecer asociaciones: Miembros participan en Proyectos
    proyecto1.add_miembro(ana)
    proyecto1.add_miembro(carlos)
    proyecto1.add_miembro(maria)

    proyecto2.add_miembro(ana)
    proyecto2.add_miembro(juan)
    proyecto2.add_miembro(maria)

    # Establecer asociaciones: Proyectos tienen lugar en Lugares
    proyecto1.add_lugar(madrid)
    proyecto1.add_lugar(remoto)

    proyecto2.add_lugar(barcelona)
    proyecto2.add_lugar(madrid)

    # Mostrar información completa
    print("="*70)
    print("PROYECTOS Y ASOCIACIONES")
    print("="*70)
    print()

    for proyecto in (proyecto1, proyecto2):
        print(proyecto)
        print()

    # Mostrar miembros y sus participaciones
    print("="*70)
    print("MIEMBROS Y SUS PARTICIPACIONES")
    print("="*70)
    print()
    for miembro in (ana, carlos, maria, juan):
        print(miembro)
    print()

    # Mostrar lugares y proyectos asociados
    print("="*70)
    print("LUGARES Y PROYECTOS ASOCIADOS")
    print("="*70)
    print()
    for lugar in (madrid, barcelona, remoto):
        print(lugar)
    print()

if __name__ == "__main__":
    main()