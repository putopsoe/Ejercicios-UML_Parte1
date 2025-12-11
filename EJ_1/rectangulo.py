from EJ_1.figura import Figura
class Rectangulo(Figura):
    def __init__(self, ancho, alto, color="naranja"):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.color = color

    def __str__(self):
        return f"Rectangulo(ancho={self.ancho}, alto={self.alto}, color={self.color})"
