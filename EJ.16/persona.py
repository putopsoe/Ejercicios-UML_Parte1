from datetime import date
from typing import Optional, List

class Persona:
    """
    nombre: str
    primer_apellido: str
    segundo_apellido: Optional[str]
    fecha_nacimiento: date
    sexo: str
    numero_identificacion: Optional[str]

    Asociaciones:
    conyuge: 0..1 Persona
    padre: 0..1 Persona
    madre: 0..1 Persona
    hijos: 0..* Persona
    """
    def __init__(
        self,
        nombre: str,
        primer_apellido: str,
        fecha_nacimiento: date,
        sexo: str,
        segundo_apellido: Optional[str] = None,
        numero_identificacion: Optional[str] = None,
    ):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion
        self.conyuge: Optional['Persona'] = None
        self.padre: Optional['Persona'] = None
        self.madre: Optional['Persona'] = None
        self.hijos: List['Persona'] = []

    def nombre_completo(self) -> str:
        apellidos = self.primer_apellido
        if self.segundo_apellido:
            apellidos += f" {self.segundo_apellido}"
        return f"{self.nombre} {apellidos}"

    def edad(self) -> int:
        today = date.today()
        born = self.fecha_nacimiento
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def casar_con(self, otra: Optional['Persona']):
        if otra is None:
            if self.conyuge:
                self.conyuge.conyuge = None
            self.conyuge = None
            return
        if self.conyuge is otra:
            return
        if self.conyuge:
            self.conyuge.conyuge = None
        self.conyuge = otra
        if otra.conyuge and otra.conyuge is not self:
            otra.conyuge.conyuge = None
        otra.conyuge = self

    def establecer_padres(self, padre: Optional['Persona'] = None, madre: Optional['Persona'] = None):
        if padre is not None:
            self.padre = padre
            if self not in padre.hijos:
                padre.hijos.append(self)
        if madre is not None:
            self.madre = madre
            if self not in madre.hijos:
                madre.hijos.append(self)

    def anadir_hijo(self, hijo: 'Persona'):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
        if hijo.padre is None and hijo.madre is None:
            if self.sexo:
                s = self.sexo.strip().lower()
                if s.startswith('h') or s == 'hombre' or s == 'h':
                    hijo.padre = self
                elif s.startswith('m') or s == 'mujer' or s == 'm':
                    hijo.madre = self

    def __str__(self):
        partes = [self.nombre_completo(), f"Edad={self.edad()}", f"Sexo={self.sexo}"]
        if self.conyuge:
            partes.append(f"Cónyuge={self.conyuge.nombre_completo()}")
        if self.padre:
            partes.append(f"Padre={self.padre.nombre_completo()}")
        if self.madre:
            partes.append(f"Madre={self.madre.nombre_completo()}")
        if self.hijos:
            hijos_nombres = ", ".join(h.nombre_completo() for h in self.hijos)
            partes.append(f"Hijos=[{hijos_nombres}]")
        return ", ".join(partes)