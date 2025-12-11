from datetime import date
from proyecto import Proyecto
from miembro_equipo import MiembroEquipo
from lugar_actuacion import LugarActuacion

def main():
    # Crear miembros del equipo
    jefe_proyecto = MiembroEquipo("Ana", "García López", roles=["Jefe de Proyecto"])
    desarrollador1 = MiembroEquipo("Carlos", "Martínez Pérez", roles=["Desarrollador", "Tester"])
    desarrollador2 = MiembroEquipo("María", "Rodríguez Silva", roles=["Desarrolladora", "Analista"])
    diseñador = MiembroEquipo("Juan", "López Fernández", roles=["Diseñador", "UX/UI"])

    # Crear lugares de actuación
    oficina_madrid = LugarActuacion(coordenada_x=40.4168, coordenada_y=-3.7038, 
                                    nombres=["Oficina Madrid", "Sede Principal"])
    oficina_barcelona = LugarActuacion(coordenada_x=41.3851, coordenada_y=2.1734,
                                       nombres=["Oficina Barcelona", "Centro de Desarrollo"])
    oficina_remota = LugarActuacion(coordenada_x=0.0, coordenada_y=0.0,
                                    nombres=["Trabajo Remoto"])

    # Crear proyecto
    proyecto = Proyecto(
        nombre="Sistema de Gestión de Proyectos",
        fecha_inicio=date(2024, 1, 15),
        fecha_fin=date(2025, 6, 30)
    )

    # Añadir miembros
    proyecto.add_miembro(jefe_proyecto)
    proyecto.add_miembro(desarrollador1)
    proyecto.add_miembro(desarrollador2)
    proyecto.add_miembro(diseñador)

    # Añadir lugares
    proyecto.add_lugar(oficina_madrid)
    proyecto.add_lugar(oficina_barcelona)
    proyecto.add_lugar(oficina_remota)

    # Mostrar información
    print(proyecto)
    print("\n" + "="*60 + "\n")

    # Información adicional
    print("Resumen:")
    print(f"Total de miembros: {len(proyecto.miembros_equipo)}")
    print(f"Total de ubicaciones: {len(proyecto.lugares_actuacion)}")
    print(f"Duración estimada: {(proyecto.fecha_fin - proyecto.fecha_inicio).days} días")

if __name__ == "__main__":
    main()