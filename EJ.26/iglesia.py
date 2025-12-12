from __future__ import annotations
from enum import Enum
from typing import List, Optional


class FormaAbside(Enum):
    SEMICIRCULAR = "Semicircular"
    EN_CORONA = "En corona"


class TecnicaCierreSimple(Enum):
    TELA_ENCERADA = "Tela encerada"
    TELA_IMPREGNADA = "Tela impregnada"


class TecnicaCierreComplejo(Enum):
    VIDRIERA_INCOLORA = "Vidriera incolora"
    VIDRIERA_COLOR = "Vidriera color"


class TipoCrucero(Enum):
    SIN_BRAZOS_SALIENTES = "Sin brazos salientes"
    CON_BRAZOS_SALIENTES = "Con brazos salientes"


class Ventana:
    def __init__(self, descripcion: str, anchura: float, altura: float):
        self.descripcion = str(descripcion)
        self.anchura = float(anchura)
        self.altura = float(altura)

    def area(self) -> float:
        return self.anchura * self.altura

    def __repr__(self):
        return f"Ventana(descripcion='{self.descripcion}', anchura={self.anchura}, altura={self.altura})"


class VentanaSimple(Ventana):
    def __init__(self, descripcion: str, anchura: float, altura: float, tiene_arco_doble: bool,
                 esta_decorada: bool, tecnica: TecnicaCierreSimple):
        super().__init__(descripcion, anchura, altura)
        self.tiene_arco_doble = bool(tiene_arco_doble)
        self.esta_decorada = bool(esta_decorada)
        self.tecnica = tecnica

    def __repr__(self):
        return (f"VentanaSimple(desc='{self.descripcion}', ancho={self.anchura}, alto={self.altura}, "
                f"arco_doble={self.tiene_arco_doble}, decorada={self.esta_decorada}, tecnica={self.tecnica.value})")


class VentanaCompleja(Ventana):
    def __init__(self, descripcion: str, anchura: float, altura: float, tecnica: TecnicaCierreComplejo):
        super().__init__(descripcion, anchura, altura)
        self.tecnica = tecnica

    def __repr__(self):
        return (f"VentanaCompleja(desc='{self.descripcion}', ancho={self.anchura}, alto={self.altura}, "
                f"tecnica={self.tecnica.value})")


class Nave:
    def __init__(self, superficie: float):
        self.superficie = float(superficie)

    def __repr__(self):
        return f"Nave(superficie={self.superficie})"


class Abside:
    def __init__(self, forma: FormaAbside):
        self.forma = forma
        self.ventanas: List[Ventana] = []

    def add_ventana(self, v: Ventana):
        if v not in self.ventanas:
            self.ventanas.append(v)

    def remove_ventana(self, v: Ventana):
        if v in self.ventanas:
            self.ventanas.remove(v)

    def ventanas_count(self) -> int:
        return len(self.ventanas)

    def __repr__(self):
        return f"Abside(forma={self.forma.value}, ventanas={len(self.ventanas)})"


class Crucero:
    def __init__(self, tipo: TipoCrucero):
        self.tipo = tipo

    def __repr__(self):
        return f"Crucero(tipo={self.tipo.value})"


class Iglesia:
    def __init__(self, nombre: str, direccion: Optional[str] = None):
        self.nombre = str(nombre)
        self.direccion = str(direccion) if direccion is not None else ""
        self.naves: List[Nave] = []
        self.absides: List[Abside] = []
        self.ventanas: List[Ventana] = []
        self.crucero: Optional[Crucero] = None

    def add_nave(self, nave: Nave):
        if nave not in self.naves:
            self.naves.append(nave)

    def add_abside(self, ab: Abside):
        if ab not in self.absides:
            self.absides.append(ab)

    def add_ventana(self, v: Ventana):
        if v not in self.ventanas:
            self.ventanas.append(v)

    def set_crucero(self, c: Crucero):
        self.crucero = c

    def is_valid(self) -> bool:
        return len(self.naves) >= 1 and len(self.absides) >= 1

    def total_ventanas(self) -> int:
        s = len(self.ventanas)
        for a in self.absides:
            s += len(a.ventanas)
        return s

    def __repr__(self):
        return (f"Iglesia(nombre={self.nombre}, naves={len(self.naves)}, absides={len(self.absides)}, "
                f"ventanas={self.total_ventanas()}, crucero={'Sí' if self.crucero else 'No'})")


class IglesiaRural(Iglesia):
    def __init__(self, nombre: str, direccion: Optional[str] = None):
        super().__init__(nombre, direccion)
        if not self.naves:
            self.add_nave(Nave(superficie=0.0))
        if not self.absides:
            self.add_abside(Abside(forma=FormaAbside.SEMICIRCULAR))

    def is_valid(self) -> bool:
        return len(self.naves) == 1 and len(self.absides) == 1


class IglesiaMonacal(Iglesia):
    def __init__(self, nombre: str, orden: Optional[str] = None, direccion: Optional[str] = None):
        super().__init__(nombre, direccion)
        self.orden = str(orden) if orden is not None else ""

    def naves_count_valid(self) -> bool:
        return 3 <= len(self.naves) <= 5

    def absides_count_valid(self) -> bool:
        return 3 <= len(self.absides) <= 5

    def is_valid(self) -> bool:
        return self.naves_count_valid() and self.absides_count_valid()

    def __repr__(self):
        return (f"IglesiaMonacal(nombre={self.nombre}, orden={self.orden}, naves={len(self.naves)}, "
                f"absides={len(self.absides)}, ventanas={self.total_ventanas()}, crucero={'Sí' if self.crucero else 'No'})")