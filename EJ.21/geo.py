from __future__ import annotations
from typing import List, Optional
import math


class EntidadGeografica:
    """Entidad geográfica con código y nombre."""
    def __init__(self, codigo: str, nombre: str):
        self.codigo = str(codigo)
        self.nombre = str(nombre)

    def __repr__(self):
        return f"EntidadGeografica(codigo={self.codigo}, nombre={self.nombre})"


class Punto(EntidadGeografica):
    """Punto definido por coordenadas X, Y (Z opcional)."""
    def __init__(self, codigo: str, nombre: str, x: float, y: float, z: Optional[float] = 0.0):
        super().__init__(codigo, nombre)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z) if z is not None else 0.0

    def coords(self):
        return (self.x, self.y, self.z)

    def __repr__(self):
        return f"Punto({self.nombre}, codigo={self.codigo}, x={self.x}, y={self.y}, z={self.z})"


class Linea(EntidadGeografica):
    """Línea definida por al menos 2 puntos."""
    def __init__(self, codigo: str, nombre: str, points: Optional[List[Punto]] = None):
        super().__init__(codigo, nombre)
        self.points: List[Punto] = list(points or [])

    def add_point(self, p: Punto):
        if p in self.points:
            return
        self.points.append(p)

    def remove_point(self, p: Punto):
        if p in self.points:
            self.points.remove(p)

    def is_valid(self) -> bool:
        return len(self.points) >= 2

    def length(self) -> float:
        if not self.is_valid():
            return 0.0
        total = 0.0
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            total += distance(p1, p2)
        return total

    def __repr__(self):
        pts = "->".join(f"({p.x},{p.y})" for p in self.points)
        return f"Linea({self.nombre}, codigo={self.codigo}, points=[{pts}], valid={self.is_valid()})"


class Area(EntidadGeografica):
    """Área definida por tres o más puntos (polígono simple)."""
    def __init__(self, codigo: str, nombre: str, points: Optional[List[Punto]] = None):
        super().__init__(codigo, nombre)
        self.points: List[Punto] = list(points or [])

    def add_point(self, p: Punto):
        if p in self.points:
            return
        self.points.append(p)

    def remove_point(self, p: Punto):
        if p in self.points:
            self.points.remove(p)

    def is_valid(self) -> bool:
        return len(self.points) >= 3

    def area(self) -> float:
        if not self.is_valid():
            return 0.0
        pts = self.points
        n = len(pts)
        s = 0.0
        for i in range(n):
            x1, y1 = pts[i].x, pts[i].y
            x2, y2 = pts[(i + 1) % n].x, pts[(i + 1) % n].y
            s += x1 * y2 - x2 * y1
        return abs(s) / 2.0

    def __repr__(self):
        pts = ", ".join(f"({p.x},{p.y})" for p in self.points)
        return f"Area({self.nombre}, codigo={self.codigo}, points=[{pts}], valid={self.is_valid()})"


def distance(a: Punto, b: Punto) -> float:
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return math.sqrt(dx * dx + dy * dy + dz * dz)