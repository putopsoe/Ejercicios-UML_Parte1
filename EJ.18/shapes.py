from typing import Optional
import math


class Forma:
    """Clase base para formas, con atributo color"""
    def __init__(self, color: str = "negro"):
        self.color = color

    def __repr__(self):
        return f"{self.__class__.__name__}(color={self.color})"


class Cuadrilatero(Forma):
    """Cuadrilátero con longitud principal (altura/longitud genérica)"""
    def __init__(self, longitud: float, color: str = "negro"):
        super().__init__(color=color)
        self.longitud = float(longitud)

    def __repr__(self):
        return f"{self.__class__.__name__}(longitud={self.longitud}, color={self.color})"


class Rectangulo(Cuadrilatero):
    """Rectángulo con longitud y anchura"""
    def __init__(self, longitud: float, anchura: float, color: str = "negro"):
        super().__init__(longitud=longitud, color=color)
        self.anchura = float(anchura)

    def area(self) -> float:
        return self.longitud * self.anchura

    def perimetro(self) -> float:
        return 2 * (self.longitud + self.anchura)

    def __repr__(self):
        return (f"Rectangulo(longitud={self.longitud}, anchura={self.anchura}, "
                f"color={self.color})")


class Cuadrado(Cuadrilatero):
    """Cuadrado: longitud representa el lado"""
    def __init__(self, longitud: float, color: str = "negro"):
        super().__init__(longitud=longitud, color=color)

    def area(self) -> float:
        return self.longitud * self.longitud

    def perimetro(self) -> float:
        return 4 * self.longitud

    def __repr__(self):
        return f"Cuadrado(longitud={self.longitud}, color={self.color})"


class Conica(Forma):
    """Forma cónica base"""
    def __init__(self, color: str = "negro"):
        super().__init__(color=color)


class Circulo(Conica):
    """Círculo definido por su diámetro"""
    def __init__(self, diametro: float, color: str = "negro"):
        super().__init__(color=color)
        self.diametro = float(diametro)

    @property
    def radio(self) -> float:
        return self.diametro / 2.0

    def area(self) -> float:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2.0 * math.pi * self.radio

    def __repr__(self):
        return (f"Circulo(diametro={self.diametro}, radio={self.radio:.3f}, "
                f"color={self.color})")


class Elipse(Conica):
    """Elipse definida por eje mayor y eje menor"""
    def __init__(self, eje_mayor: float, eje_menor: float, color: str = "negro"):
        super().__init__(color=color)
        self.eje_mayor = float(eje_mayor)
        self.eje_menor = float(eje_menor)

    def area(self) -> float:
        a = self.eje_mayor / 2.0
        b = self.eje_menor / 2.0
        return math.pi * a * b

    def perimetro(self) -> float:
        a = self.eje_mayor / 2.0
        b = self.eje_menor / 2.0
        h = ((a - b) ** 2) / ((a + b) ** 2) if (a + b) != 0 else 0
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def __repr__(self):
        return (f"Elipse(eje_mayor={self.eje_mayor}, eje_menor={self.eje_menor}, "
                f"color={self.color})")