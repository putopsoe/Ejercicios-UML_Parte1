from datetime import date
from typing import Optional, List
from miembro_equipo import MiembroEquipo
from lugar_actuacion import LugarActuacion

class Proyecto:
    """
    Atributos:
    - nombre: texto (obligatorio)
    - fecha_inicio: date (obligatorio)
    - fecha_fin: date (opcional, 0..1)
    - miembros_equipo: lista de MiembroEquipo
    - lugares_actuacion: lista de LugarActuacion
    """
    def __init__(self, nombre: str, fecha_inicio: date, fecha_fin: Optional[date] = None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.miembros_equipo: List[MiembroEquipo] = []
        self.lugares_actuacion: List[LugarActuacion] = []

    def add_miembro(self, miembro: MiembroEquipo):
        """Añade un miembro al equipo del proyecto."""
        if miembro not in self.miembros_equipo:
            self.miembros_equipo.append(miembro)

    def add_lugar(self, lugar: LugarActuacion):
        """Añade un lugar de actuación al proyecto."""
        if lugar not in self.lugares_actuacion:
            self.lugares_actuacion.append(lugar)

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
            f"Nombre: {self.nombre}",
            f"Fecha de inicio: {self.fecha_inicio.strftime('%d/%m/%Y')}",
            f"Fecha de fin: {fecha_fin_str}",
            f"Estado: {self.estado()}",
            f"Miembros del equipo ({len(self.miembros_equipo)}):"
        ]
        for miembro in self.miembros_equipo:
            partes.append(f"  - {miembro}")
        partes.append(f"Lugares de actuación ({len(self.lugares_actuacion)}):")
        for lugar in self.lugares_actuacion:
            partes.append(f"  - {lugar}")
        return "\n".join(partes)