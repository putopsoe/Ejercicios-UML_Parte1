from typing import List, Optional
from math import hypot

class Point:
    """Punto en 2D. Puede pertenecer a varios polígonos."""
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
        # Lista de polígonos a los que pertenece este punto
        self.polygons: List['Polygon'] = []

    def add_polygon(self, poly: 'Polygon'):
        if poly not in self.polygons:
            self.polygons.append(poly)

    def remove_polygon(self, poly: 'Polygon'):
        if poly in self.polygons:
            self.polygons.remove(poly)

    def coords(self):
        return (self.x, self.y)

    def __repr__(self):
        names = [p.name for p in self.polygons] if self.polygons else []
        return f"Point(x={self.x}, y={self.y}, polygons={names})"


class Polygon:
    """Polígono genérico, definido por al menos 3 puntos.
    Ahora un mismo punto puede pertenecer a varios polígonos.
    """
    def __init__(self, name: Optional[str] = None):
        self.name = name or "Polygon"
        self.points: List[Point] = []

    def add_point(self, p: Point):
        if p in self.points:
            return
        self.points.append(p)
        p.add_polygon(self)

    def remove_point(self, p: Point):
        if p in self.points:
            self.points.remove(p)
            p.remove_polygon(self)

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
            x2, y2 = pts[(i + 1) % n].coords()
            s += x1 * y2 - x2 * y1
        return abs(s) / 2.0

    def perimeter(self) -> float:
        if len(self.points) < 2:
            return 0.0
        perim = 0.0
        n = len(self.points)
        for i in range(n):
            x1, y1 = self.points[i].coords()
            x2, y2 = self.points[(i + 1) % n].coords()
            perim += hypot(x2 - x1, y2 - y1)
        return perim

    def __repr__(self):
        pts = ", ".join(f"({p.x},{p.y})" for p in self.points)
        return f"{self.name}: [{pts}] (valid={self.is_valid()})"