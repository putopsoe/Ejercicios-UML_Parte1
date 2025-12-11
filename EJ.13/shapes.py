from typing import Optional, List
from math import hypot

class Point:
    """Punto en 2D. Pertenece a, como mucho, un solo Polygon."""
    def __init__(self, x: float, y: float, polygon: Optional['Polygon'] = None):
        self.x = float(x)
        self.y = float(y)
        self.polygon: Optional['Polygon'] = None
        if polygon is not None:
            self.set_polygon(polygon)

    def set_polygon(self, polygon: 'Polygon'):
        if self.polygon is polygon:
            return
        if self.polygon is not None and self.polygon is not polygon:
            raise ValueError("Este punto ya pertenece a otro polígono.")
        self.polygon = polygon

    def remove_polygon(self):
        self.polygon = None

    def coords(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, polygon={'None' if self.polygon is None else self.polygon.name})"


class Polygon:
    """Polígono definido por al menos 3 puntos. Un punto sólo puede pertenecer a un único polígono."""
    def __init__(self, name: str = None):
        self.name = name or "Polygon"
        self.points: List[Point] = []

    def add_point(self, p: Point):
        if p in self.points:
            return
        # Comprueba pertenencia única
        if p.polygon is not None and p.polygon is not self:
            raise ValueError(f"El punto {p} ya pertenece al polígono '{p.polygon.name}'.")
        self.points.append(p)
        p.set_polygon(self)

    def remove_point(self, p: Point):
        if p in self.points:
            self.points.remove(p)
            p.remove_polygon()

    def is_valid(self) -> bool:
        return len(self.points) >= 3

    def area(self) -> float:
        """Área por fórmula de lazo (shoelace). Devuelve 0.0 si no es válido."""
        if not self.is_valid():
            return 0.0
        pts = self.points
        n = len(pts)
        s = 0.0
        for i in range(n):
            x1, y1 = pts[i].coords()
            x2, y2 = pts[(i+1) % n].coords()
            s += x1 * y2 - x2 * y1
        return abs(s) / 2.0

    def perimeter(self) -> float:
        if len(self.points) < 2:
            return 0.0
        perim = 0.0
        n = len(self.points)
        for i in range(n):
            x1, y1 = self.points[i].coords()
            x2, y2 = self.points[(i+1) % n].coords()
            perim += hypot(x2 - x1, y2 - y1)
        return perim

    def __repr__(self):
        pts = ", ".join(f"({p.x},{p.y})" for p in self.points)
        return f"{self.name}: [{pts}] (valid={self.is_valid()})"