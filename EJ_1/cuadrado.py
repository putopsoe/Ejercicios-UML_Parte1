from EJ_1.figura import Figura
class Cuadrado(Figura):
    def __init__(self, lado, color="azul"):
        super().__init__()
        self.lado = lado
        self.color = color

    def __str__(self):
        return f"Cuadrado(lado={self.lado}, color={self.color})"
