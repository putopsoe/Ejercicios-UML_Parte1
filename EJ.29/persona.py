from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List, Optional


class DocumentoTipo(Enum):
    LIBRO = "Libro"
    ARTICULO = "Artículo"
    INFORME = "Informe"
    OTRO = "Otro"


class Sexo(Enum):
    HOMBRE = "Hombre"
    MUJER = "Mujer"
    OTRO = "Otro"


class Lugar:
    def __init__(self, nombre: str, direccion: Optional[str] = None, pais: Optional[str] = None):
        self.nombre = str(nombre)
        self.direccion = str(direccion) if direccion is not None else ""
        self.pais = str(pais) if pais is not None else ""

    def __repr__(self):
        return f"Lugar(nombre={self.nombre}, direccion={self.direccion}, pais={self.pais})"


@dataclass
class Documento:
    titulo: str
    tipo: DocumentoTipo
    fecha_publicacion: Optional[date] = None
    autores: Optional[List[str]] = None
    identificador: Optional[str] = None

    def __repr__(self):
        id_str = f", id={self.identificador}" if self.identificador else ""
        pub = self.fecha_publicacion.isoformat() if self.fecha_publicacion else "fecha?"
        autores_str = ", ".join(self.autores) if self.autores else "desconocido"
        return f"Documento({self.titulo}, {self.tipo.value}, {pub}, autores=[{autores_str}]{id_str})"


class Evento:
    def __init__(self, nombre: str, fecha: Optional[date] = None, descripcion: Optional[str] = None):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion or ""
        self.participantes: List[Persona] = []

    def add_participante(self, persona: "Persona"):
        if persona not in self.participantes:
            self.participantes.append(persona)
            persona.participaciones.append(self)

    def __repr__(self):
        fstr = self.fecha.isoformat() if self.fecha else "fecha?"
        return f"Evento({self.nombre}, fecha={fstr}, participantes={len(self.participantes)})"


class Ocupacion:
    def __init__(self, nombre: str, desde: Optional[date] = None, hasta: Optional[date] = None, organizacion: Optional[str] = None):
        self.nombre = nombre
        self.desde = desde
        self.hasta = hasta
        self.organizacion = organizacion or ""

    def esta_activa(self, hoy: Optional[date] = None) -> bool:
        from datetime import date as _date
        hoy = hoy or _date.today()
        desde_ok = self.desde is None or self.desde <= hoy
        hasta_ok = self.hasta is None or self.hasta >= hoy
        return desde_ok and hasta_ok

    def __repr__(self):
        desde = self.desde.isoformat() if self.desde else "desde?"
        hasta = self.hasta.isoformat() if self.hasta else "hasta?"
        org = f", org={self.organizacion}" if self.organizacion else ""
        return f"Ocupacion({self.nombre}{org}, {desde} - {hasta})"


class Visita:
    def __init__(self, lugar: Lugar, fecha_inicio: Optional[date] = None, fecha_fin: Optional[date] = None, proposito: Optional[str] = None):
        self.lugar = lugar
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.proposito = proposito or ""

    def __repr__(self):
        fi = self.fecha_inicio.isoformat() if self.fecha_inicio else "?"
        ff = self.fecha_fin.isoformat() if self.fecha_fin else "?"
        return f"Visita(lugar={self.lugar.nombre}, {fi} - {ff}, proposito={self.proposito})"


class Lectura:
    def __init__(self, documento: Documento, fecha_lectura: Optional[date] = None, notas: Optional[str] = None):
        self.documento = documento
        self.fecha_lectura = fecha_lectura
        self.notas = notas or ""

    def __repr__(self):
        fstr = self.fecha_lectura.isoformat() if self.fecha_lectura else "fecha?"
        return f"Lectura(doc={self.documento.titulo}, fecha={fstr})"


class Contacto:
    def __init__(self, otra_persona: "Persona", relacion: Optional[str] = None, desde: Optional[date] = None, hasta: Optional[date] = None):
        self.otra_persona = otra_persona
        self.relacion = relacion or ""
        self.desde = desde
        self.hasta = hasta

    def activa(self, hoy: Optional[date] = None) -> bool:
        from datetime import date as _date
        hoy = hoy or _date.today()
        desde_ok = self.desde is None or self.desde <= hoy
        hasta_ok = self.hasta is None or self.hasta >= hoy
        return desde_ok and hasta_ok

    def __repr__(self):
        desde = self.desde.isoformat() if self.desde else "?"
        hasta = self.hasta.isoformat() if self.hasta else "?"
        return f"Contacto(persona={self.otra_persona.nombre_completo()}, relacion={self.relacion}, {desde} - {hasta})"


class Persona:
    def __init__(
        self,
        nombre: str,
        primer_apellido: str,
        fecha_nacimiento: date,
        sexo: Sexo,
        segundo_apellido: Optional[str] = None,
        titulo: Optional[str] = None,
        lugar_nacimiento: Optional[Lugar] = None,
        fecha_defuncion: Optional[date] = None,
        lugar_defuncion: Optional[Lugar] = None
    ):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido or ""
        self.titulo = titulo or ""
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_defuncion = fecha_defuncion
        self.lugar_defuncion = lugar_defuncion
        self.sexo = sexo
        self.ocupaciones: List[Ocupacion] = []
        self.contactos: List[Contacto] = []
        self.visitas: List[Visita] = []
        self.lecturas: List[Lectura] = []
        self.participaciones: List[Evento] = []
        self.documentos_propios: List[Documento] = []

    def nombre_completo(self) -> str:
        apellidos = self.primer_apellido + (f" {self.segundo_apellido}" if self.segundo_apellido else "")
        return f"{self.nombre} {apellidos}"

    def anadir_ocupacion(self, ocupacion: Ocupacion):
        if ocupacion not in self.ocupaciones:
            self.ocupaciones.append(ocupacion)

    def anadir_contacto(self, otra_persona: "Persona", relacion: Optional[str] = None, desde: Optional[date] = None, hasta: Optional[date] = None):
        c = Contacto(otra_persona, relacion=relacion, desde=desde, hasta=hasta)
        if c not in self.contactos:
            self.contactos.append(c)
        reciprocal = Contacto(self, relacion=relacion, desde=desde, hasta=hasta)
        if reciprocal not in otra_persona.contactos:
            otra_persona.contactos.append(reciprocal)

    def anadir_visita(self, visita: Visita):
        if visita not in self.visitas:
            self.visitas.append(visita)

    def anadir_lectura(self, lectura: Lectura):
        if lectura not in self.lecturas:
            self.lecturas.append(lectura)

    def participar_en(self, evento: Evento):
        evento.add_participante(self)

    def publicar_documento(self, documento: Documento):
        if documento not in self.documentos_propios:
            self.documentos_propios.append(documento)

    def edad(self, hoy: Optional[date] = None) -> Optional[int]:
        from datetime import date as _date
        hoy = hoy or _date.today()
        born = self.fecha_nacimiento
        if self.fecha_defuncion:
            end = self.fecha_defuncion
        else:
            end = hoy
        return end.year - born.year - ((end.month, end.day) < (born.month, born.day))

    def ocupaciones_activas(self, hoy: Optional[date] = None) -> List[Ocupacion]:
        return [o for o in self.ocupaciones if o.esta_activa(hoy)]

    def __repr__(self):
        return (f"Persona({self.nombre_completo()}, titulo={self.titulo}, nacimiento={self.fecha_nacimiento.isoformat()}, "
                f"ocupaciones={len(self.ocupaciones)}, contactos={len(self.contactos)}, lecturas={len(self.lecturas)})")