from enum import Enum
from typing import List, Dict, Optional


class TipoElemento(Enum):
    PORTADA = "Portada"
    PUERTA = "Puerta"
    VENTANA = "Ventana"
    BALCON = "Balcón"
    OTRO = "Otro"


class ElementoEstructural:
    def __init__(self, codigo: str, tipo: TipoElemento, descripcion: Optional[str] = None):
        self.codigo = str(codigo)
        self.tipo = tipo
        self.descripcion = descripcion or ""

    def __repr__(self):
        return f"ElementoEstructural(codigo={self.codigo}, tipo={self.tipo.value})"


class Edificio:
    def __init__(self, nombre: str, numero: Optional[str] = None, plantas: Optional[int] = None):
        self.nombre = str(nombre)
        self.numero = str(numero) if numero is not None else None
        self.plantas = int(plantas) if plantas is not None else None
        self.elementos: List[ElementoEstructural] = []
        self.espacio: Optional["EspacioAbierto"] = None

    def add_elemento(self, elemento: ElementoEstructural):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def remover_elemento(self, elemento: ElementoEstructural):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def contar_elementos_por_tipo(self) -> Dict[TipoElemento, int]:
        conteo: Dict[TipoElemento, int] = {}
        for e in self.elementos:
            conteo[e.tipo] = conteo.get(e.tipo, 0) + 1
        return conteo

    def riqueza_fachada(self) -> int:
        return len(self.elementos)

    def __repr__(self):
        n = f", numero={self.numero}" if self.numero is not None else ""
        p = f", plantas={self.plantas}" if self.plantas is not None else ""
        return f"Edificio(nombre={self.nombre}{n}{p}, elementos={len(self.elementos)})"


class EspacioAbierto:
    def __init__(self, nombre: str):
        self.nombre = str(nombre)
        self.edificios: List[Edificio] = []

    def add_edificio(self, edificio: Edificio):
        if edificio not in self.edificios:
            self.edificios.append(edificio)
            edif_actual = edificio.espacio
            if edif_actual is not self:
                edificio.espacio = self

    def remove_edificio(self, edificio: Edificio):
        if edificio in self.edificios:
            self.edificios.remove(edificio)
            if edificio.espacio is self:
                edificio.espacio = None

    def contar_edificios(self) -> int:
        return len(self.edificios)

    def contar_elementos_total(self) -> int:
        total = 0
        for e in self.edificios:
            total += e.riqueza_fachada()
        return total

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre={self.nombre}, edificios={len(self.edificios)})"


class Calle(EspacioAbierto):
    def __init__(self, nombre: str, longitud: Optional[float] = None):
        super().__init__(nombre)
        self.longitud = float(longitud) if longitud is not None else None

    def __repr__(self):
        longitud_str = f", longitud={self.longitud}" if self.longitud is not None else ""
        return f"Calle(nombre={self.nombre}{longitud_str}, edificios={len(self.edificios)})"


class Plaza(EspacioAbierto):
    def __init__(self, nombre: str, superficie: Optional[float] = None):
        super().__init__(nombre)
        self.superficie = float(superficie) if superficie is not None else None

    def __repr__(self):
        superficie_str = f", superficie={self.superficie}" if self.superficie is not None else ""
        return f"Plaza(nombre={self.nombre}{superficie_str}, edificios={len(self.edificios)})"


class Ciudad:
    def __init__(self, nombre: str, pais: str):
        self.nombre = str(nombre)
        self.pais = str(pais)
        self.espacios: List[EspacioAbierto] = []

    def add_espacio(self, espacio: EspacioAbierto):
        if espacio not in self.espacios:
            self.espacios.append(espacio)

    def contar_espacios(self) -> int:
        return len(self.espacios)

    def contar_edificios(self) -> int:
        total = 0
        for esp in self.espacios:
            total += esp.contar_edificios()
        return total

    def contar_elementos_por_tipo(self) -> Dict[TipoElemento, int]:
        conteo: Dict[TipoElemento, int] = {}
        for esp in self.espacios:
            for ed in esp.edificios:
                for el in ed.elementos:
                    conteo[el.tipo] = conteo.get(el.tipo, 0) + 1
        return conteo

    def edificios_ordenados_por_riqueza(self, reverse: bool = True) -> List[Edificio]:
        todos: List[Edificio] = []
        for esp in self.espacios:
            todos.extend(esp.edificios)
        return sorted(todos, key=lambda ed: ed.riqueza_fachada(), reverse=reverse)

    def __repr__(self):
        return f"Ciudad({self.nombre}, {self.pais}, espacios={len(self.espacios)})"