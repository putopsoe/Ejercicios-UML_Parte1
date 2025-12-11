from typing import Optional, List

class MiembroEquipo:
    """
    Atributos:
    - nombre: texto (obligatorio)
    - apellidos: texto (obligatorio)
    - rol: lista de textos (0..* roles)
    """
    def __init__(self, nombre: str, apellidos: str, roles: Optional[List[str]] = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.roles = roles or []

    def add_rol(self, rol: str):
        """Añade un rol a la persona si no existe ya."""
        if rol not in self.roles:
            self.roles.append(rol)

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellidos}"

    def __str__(self):
        roles_str = ", ".join(self.roles) if self.roles else "Sin rol asignado"
        return f"MiembroEquipo: {self.nombre_completo()} | Roles: {roles_str}"