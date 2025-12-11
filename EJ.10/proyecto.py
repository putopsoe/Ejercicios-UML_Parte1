from datetime import date
from typing import Optional, List

class Proyecto:
    """
    Atributos:
    - nombre: texto (1)
    - fecha_inicio: date (1)
    - fecha_fin: date (0..1)
    
    Asociaciones:
    - miembros_equipo: 1..* MiembroEquipo (participan en el proyecto)
    - lugares_actuacion: 0..* LugarActuacion (donde se realiza el proyecto)
    """
    def __init__(self, nombre: str, fecha_inicio: date, fecha_fin: Optional[date] = None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.miembros_equipo: List["MiembroEquipo"] = []
        self.lugares_actuacion: List['LugarActuacion'] = []

    def add_miembro(self, miembro: 'MiembroEquipo'):
        """Asocia un miembro al proyecto (relación bidireccional)."""
        if miembro not in self.miembros_equipo:
            self.miembros_equipo.append(miembro)
            if self not in miembro.participa_en:
                miembro.participa_en.append(self)

    def add_lugar(self, lugar: 'LugarActuacion'):
        """Asocia un lugar de actuación al proyecto (relación bidireccional)."""
        if lugar not in self.lugares_actuacion:
            self.lugares_actuacion.append(lugar)
            if self not in lugar.proyectos:
                lugar.proyectos.append(self)

    def estado(self) -> str:
        """Retorna el estado del proyecto."""
        today = date.today()
        if today < self.fecha_inicio:
            return "No iniciado"
        elif self.fecha_fin and today > self.fecha_fin:
            return "Finalizado"
        else:
            return "En curso"

    def __str__(self):
        fecha_fin_str = self.fecha_fin.strftime("%d/%m/%Y") if self.fecha_fin else "—"
        partes = [
            f"Proyecto: {self.nombre}",
            f"Fecha de inicio: {self.fecha_inicio.strftime('%d/%m/%Y')}",
            f"Fecha de fin: {fecha_fin_str}",
            f"Estado: {self.estado()}",
            f"Miembros del equipo ({len(self.miembros_equipo)}):"
        ]
        for miembro in self.miembros_equipo:
            partes.append(f"  - {miembro.nombre_completo()} ({', '.join(miembro.roles) if miembro.roles else 'Sin rol'})")
        partes.append(f"Lugares de actuación ({len(self.lugares_actuacion)}):")
        for lugar in self.lugares_actuacion:
            nombres = ", ".join(lugar.nombres) if lugar.nombres else "Sin nombre"
            partes.append(f"  - {nombres} ({lugar.coordenada_x}, {lugar.coordenada_y})")
        return "\n".join(partes)