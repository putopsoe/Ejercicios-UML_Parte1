from typing import Optional, List

class MiembroEquipo:
    """
    Atributos:
    - nombre: texto (1)
    - apellidos: texto (1)
    - rol: lista de textos (0..*)
    
    Asociaciones:
    - participa_en: lista de Proyecto (participación en proyectos)
    """
    def __init__(self, nombre: str, apellidos: str, roles: Optional[List[str]] = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.roles = roles or []
        self.participa_en: List['Proyecto'] = []

    def add_rol(self, rol: str):
        """Añade un rol si no existe ya."""
        if rol not in self.roles:
            self.roles.append(rol)

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellidos}"

    def participar_en(self, proyecto: 'Proyecto'):
        """Asocia este miembro a un proyecto."""
        if proyecto not in self.participa_en:
            self.participa_en.append(proyecto)
            if self not in proyecto.miembros_equipo:
                proyecto.miembros_equipo.append(self)

    def __str__(self):
        roles_str = ", ".join(self.roles) if self.roles else "Sin rol"
        proyectos_str = ", ".join(p.nombre for p in self.participa_en) if self.participa_en else "—"
        return f"MiembroEquipo: {self.nombre_completo()} | Roles: {roles_str} | Proyectos: {proyectos_str}"