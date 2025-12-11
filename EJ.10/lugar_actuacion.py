from typing import Optional, List

class LugarActuacion:
    """
    Atributos:
    - nombres: lista de textos (0..*)
    - coordenada_x: número (1)
    - coordenada_y: número (1)
    
    Asociaciones:
    - proyectos: lista de Proyecto (proyectos que se realizan aquí)
    """
    def __init__(self, coordenada_x: float, coordenada_y: float, nombres: Optional[List[str]] = None):
        self.nombres = nombres or []
        self.coordenada_x = float(coordenada_x)
        self.coordenada_y = float(coordenada_y)
        self.proyectos: List['Proyecto'] = []

    def add_nombre(self, nombre: str):
        """Añade un nombre al lugar si no existe ya."""
        if nombre not in self.nombres:
            self.nombres.append(nombre)

    def __str__(self):
        nombres_str = ", ".join(self.nombres) if self.nombres else "Sin nombre"
        proyectos_str = ", ".join(p.nombre for p in self.proyectos) if self.proyectos else "—"
        return f"LugarActuacion: {nombres_str} ({self.coordenada_x}, {self.coordenada_y}) | Proyectos: {proyectos_str}"