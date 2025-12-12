from enum import Enum
from typing import Optional


class FormaImpresion(Enum):
    MANUSCRITO = "Manuscrito"
    IMPRESO = "Impreso"


class TecnicaEncuadernacion(Enum):
    COSIDO = "Cosido"
    ENCUADERNADO = "Encuadernado"


class Libro:
    """
    Formal:
      - numero_hojas: Número (cantidad de hojas que forman el volumen)
      - forma_impresion: FormaImpresion (manuscrito o impreso)
      - tecnica_encuadernacion: TecnicaEncuadernacion (cosido o encuadernado)

    Invariante:
      - numero_hojas debe ser un entero positivo.
    """
    def __init__(self, numero_hojas: int, forma_impresion: FormaImpresion,
                 tecnica_encuadernacion: TecnicaEncuadernacion, identificador: Optional[str] = None):
        if not isinstance(numero_hojas, int) or numero_hojas <= 0:
            raise ValueError("numero_hojas debe ser un entero positivo.")
        self.numero_hojas = numero_hojas
        self.forma_impresion = forma_impresion
        self.tecnica_encuadernacion = tecnica_encuadernacion
        self.identificador = str(identificador) if identificador is not None else None

    def __repr__(self):
        id_str = f", id={self.identificador}" if self.identificador else ""
        return (f"Libro(numero_hojas={self.numero_hojas}, "
                f"forma_impresion={self.forma_impresion.value}, "
                f"tecnica_encuadernacion={self.tecnica_encuadernacion.value}{id_str})")


class Muestra:
    """
    Formal:
      - fraccion_total: Número (fracción del conjunto que constituye la muestra)
      - metodo_extraccion: texto (método usado para extraerla)

    Invariante:
      - 0 < fraccion_total <= 1
    """
    def __init__(self, fraccion_total: float, metodo_extraccion: str, identificador: Optional[str] = None):
        try:
            f = float(fraccion_total)
        except Exception:
            raise ValueError("fraccion_total debe ser un número.")
        if not (0 < f <= 1.0):
            raise ValueError("fraccion_total debe estar en el rango (0, 1].")
        self.fraccion_total = f
        self.metodo_extraccion = str(metodo_extraccion)
        self.identificador = str(identificador) if identificador is not None else None

    def porcentaje(self) -> float:
        return self.fraccion_total * 100.0

    def __repr__(self):
        id_str = f", id={self.identificador}" if self.identificador else ""
        return (f"Muestra(fraccion_total={self.fraccion_total}, metodo='{self.metodo_extraccion}'{id_str})")