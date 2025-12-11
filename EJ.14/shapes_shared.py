from typing import List, Optional
from math import hypot

class PointShared:
    """Punto en 2D. Puede pertenecer a varios polígonos/triángulos."""
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
        self.polygons: List['Triangle'] = []

    def add_polygon(self, poly: 'Triangle'):
        if poly not in self.polygons:
            self.polygons.append(poly)

    def remove_polygon(self, poly: 'Triangle'):
        if poly in self.polygons:
            self.polygons.remove(poly)

    def coords(self):
        return (self.x, self.y)

    def __repr__(self):
        names = [p.name for p in self.polygons] if self.polygons else []
        return f"PointShared(x={self.x}, y={self.y}, polygons={names})"


class Triangle:
    """
    Triángulo definido por exactamente 3 PointShared.
    Los puntos pueden ser compartidos por otros triángulos (para representar lados comunes).
    """
    def __init__(self, name: Optional[str] = None):
        self.name = name or "Triangle"
        self.points: List[PointShared] = []

    def add_point(self, p: PointShared):
        if p in self.points:
            return
        if len(self.points) >= 3:
            raise ValueError("Un triángulo sólo puede tener 3 puntos.")
        self.points.append(p)
        p.add_polygon(self)

    def remove_point(self, p: PointShared):
        if p in self.points:
            self.points.remove(p)
            p.remove_polygon(self)

    def is_valid(self) -> bool:
        return len(self.points) == 3

    def area(self) -> float:
        """Área por fórmula de lazo (shoelace) para 3 puntos; 0 si inválido."""
        if not self.is_valid():
            return 0.0
        (x1, y1), (x2, y2), (x3, y3) = (p.coords() for p in self.points)
        return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0

    def perimeter(self) -> float:
        if not self.is_valid():
            return 0.0
        per = 0.0
        pts = self.points
        for i in range(3):
            x1, y1 = pts[i].coords()
            x2, y2 = pts[(i+1) % 3].coords()
            per += hypot(x2 - x1, y2 - y1)
        return per

    def __repr__(self):
        pts = ", ".join(f"({p.x},{p.y})" for p in self.points)
        return f"{self.name}: [{pts}] (valid={self.is_valid()})"