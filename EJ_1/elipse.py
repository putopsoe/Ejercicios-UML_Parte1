from EJ_1.figura import Figura
class Elipse(Figura):
    def __init__(self, radio_mayor, radio_menor, color="amarillo"):
        super().__init__()
        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor
        self.color = color

    def __str__(self):
        return f"Elipse(radio_mayor={self.radio_mayor}, radio_menor={self.radio_menor}, color={self.color})"
