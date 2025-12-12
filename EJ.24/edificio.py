from __future__ import annotations
from datetime import date
from typing import Optional, List


class UsoEdificio:
    """
    Clase base para representar un uso del edificio en un periodo de tiempo.
    Fecha de fin None significa que el uso está en curso.
    """
    def __init__(self, fecha_inicio: date, fecha_fin: Optional[date] = None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def cerrar(self, fecha: date):
        self.fecha_fin = fecha

    def esta_activo(self, hoy: Optional[date] = None) -> bool:
        if hoy is None:
            hoy = date.today()
        inicio_ok = self.fecha_inicio <= hoy
        fin_ok = self.fecha_fin is None or self.fecha_fin >= hoy
        return inicio_ok and fin_ok

    def periodo(self) -> str:
        fin = self.fecha_fin.isoformat() if self.fecha_fin else "en curso"
        return f"{self.fecha_inicio.isoformat()} - {fin}"

    def tipo(self) -> str:
        return "Uso"

    def __repr__(self):
        return f"{self.tipo()}({self.periodo()})"


class Hospital(UsoEdificio):
    def __init__(self, fecha_inicio: date, fecha_fin: Optional[date] = None, camas: Optional[int] = None):
        super().__init__(fecha_inicio, fecha_fin)
        self.camas = int(camas) if camas is not None else None

    def tipo(self) -> str:
        return "Hospital"

    def __repr__(self):
        camas = f", camas={self.camas}" if self.camas is not None else ""
        return f"{self.tipo()}({self.periodo()}{camas})"


class Escuela(UsoEdificio):
    def __init__(self, fecha_inicio: date, fecha_fin: Optional[date] = None, plazas: Optional[int] = None):
        super().__init__(fecha_inicio, fecha_fin)
        self.plazas = int(plazas) if plazas is not None else None

    def tipo(self) -> str:
        return "Escuela"

    def __repr__(self):
        plazas = f", plazas={self.plazas}" if self.plazas is not None else ""
        return f"{self.tipo()}({self.periodo()}{plazas})"


class Vivienda(UsoEdificio):
    def __init__(self, fecha_inicio: date, fecha_fin: Optional[date] = None, unidades: Optional[int] = None):
        super().__init__(fecha_inicio, fecha_fin)
        self.unidades = int(unidades) if unidades is not None else None

    def tipo(self) -> str:
        return "Vivienda"

    def __repr__(self):
        unidades = f", unidades={self.unidades}" if self.unidades is not None else ""
        return f"{self.tipo()}({self.periodo()}{unidades})"


class Edificio:
    """
    Modelo de Edificio que puede tener múltiples usos en distintos periodos
    o simultáneamente (lista de UsoEdificio).
    """
    def __init__(self, nombre: str, direccion: Optional[str] = None):
        self.nombre = nombre
        self.direccion = direccion or ""
        self.usos: List[UsoEdificio] = []

    def add_uso(self, uso: UsoEdificio):
        if uso not in self.usos:
            self.usos.append(uso)

    def remove_uso(self, uso: UsoEdificio):
        if uso in self.usos:
            self.usos.remove(uso)

    def usos_actuales(self, hoy: Optional[date] = None) -> List[UsoEdificio]:
        return [u for u in self.usos if u.esta_activo(hoy)]

    def usos_historicos(self, hoy: Optional[date] = None) -> List[UsoEdificio]:
        if hoy is None:
            hoy = date.today()
        return [u for u in self.usos if u.fecha_fin is not None and u.fecha_fin < hoy]

    def cerrar_uso(self, uso: UsoEdificio, fecha: date):
        if uso in self.usos:
            uso.cerrar(fecha)

    def reemplazar_uso(self, uso_viejo: UsoEdificio, uso_nuevo: UsoEdificio):
        if uso_viejo in self.usos:
            idx = self.usos.index(uso_viejo)
            uso_viejo.cerrar(uso_nuevo.fecha_inicio)
            self.usos.insert(idx + 1, uso_nuevo)
        else:
            self.add_uso(uso_nuevo)

    def __repr__(self):
        direccion = f", direccion={self.direccion}" if self.direccion else ""
        return f"Edificio(nombre={self.nombre}{direccion}, usos={len(self.usos)})"