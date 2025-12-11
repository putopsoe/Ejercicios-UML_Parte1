from typing import Optional, List

class LugarActuacion:
    """
    Atributos:
    - nombres: lista de textos (0..* nombres)
    - coordenada_x: número (obligatorio)
    - coordenada_y: número (obligatorio)
    """
    def __init__(self, coordenada_x: float, coordenada_y: float, nombres: Optional[List[str]] = None):
        self.nombres = nombres or []
        self.coordenada_x = float(coordenada_x)
        self.coordenada_y = float(coordenada_y)

    def add_nombre(self, nombre: str):
        """Añade un nombre al lugar si no existe ya."""
        if nombre not in self.nombres:
            self.nombres.append(nombre)

    def __str__(self):
        nombres_str = ", ".join(self.nombres) if self.nombres else "Sin nombre"
        return f"LugarActuacion: {nombres_str} ({self.coordenada_x}, {self.coordenada_y})"