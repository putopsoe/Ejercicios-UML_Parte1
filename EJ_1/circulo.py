from EJ_1.figura import Figura
class Circulo(Figura):
    def __init__(self, radio, color="rojo"):
        super().__init__()
        self.radio = radio
        self.color = color

    def __str__(self):
        return f"Circulo(radio={self.radio}, color={self.color})"
