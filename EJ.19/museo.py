from __future__ import annotations
from datetime import date
from typing import List, Optional
from enum import Enum


class EstadoObjeto(Enum):
    NUEVO = "Nuevo"
    BUENO = "Bueno"
    DETERIORADO = "Deteriorado"
    EN_RESTAURACION = "En restauración"
    RESTAURADO = "Restaurado"


class Tematica(Enum):
    INFANTIL = "Infantil"
    NARRATIVA = "Narrativa"
    ENSAYO = "Ensayo"
    POESIA = "Poesía"
    ARQUEOLOGIA = "Arqueología"
    HISTORIA = "Historia"


class Origen(Enum):
    HALLAZGO = "Hallazgo"
    DONACION = "Donación"
    COMPRA = "Compra"


class Edificio:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.plantas: List[Planta] = []

    def add_planta(self, planta: "Planta"):
        if planta not in self.plantas:
            self.plantas.append(planta)
            planta.edificio = self

    def __repr__(self):
        return f"Edificio({self.nombre}, {self.direccion}, plantas={len(self.plantas)})"


class Planta:
    def __init__(self, numero: int):
        self.numero = int(numero)
        self.ubicaciones: List[Ubicacion] = []
        self.edificio: Optional[Edificio] = None

    def add_ubicacion(self, u: "Ubicacion"):
        if u not in self.ubicaciones:
            self.ubicaciones.append(u)
            u.planta = self

    def __repr__(self):
        return f"Planta(numero={self.numero}, ubicaciones={len(self.ubicaciones)})"


class Ubicacion:
    def __init__(self, codigo: str):
        self.codigo = str(codigo)
        self.objetos: List[Objeto] = []
        self.planta: Optional[Planta] = None

    def add_objeto(self, obj: "Objeto"):
        if obj not in self.objetos:
            self.objetos.append(obj)
            if obj.ubicacion is not self:
                obj.ubicacion = self

    def remove_objeto(self, obj: "Objeto"):
        if obj in self.objetos:
            self.objetos.remove(obj)
            if obj.ubicacion is self:
                obj.ubicacion = None

    def __repr__(self):
        return f"Ubicacion(codigo={self.codigo}, objetos={len(self.objetos)})"


class Sala(Ubicacion):
    def __init__(self, codigo: str, nombre: str, esta_abierta_al_publico: bool = True):
        super().__init__(codigo)
        self.nombre = nombre
        self.esta_abierta_al_publico = bool(esta_abierta_al_publico)

    def __repr__(self):
        return f"Sala({self.nombre}, codigo={self.codigo}, abierta={self.esta_abierta_al_publico})"


class Almacen(Ubicacion):
    def __init__(self, codigo: str, nombre: str):
        super().__init__(codigo)
        self.nombre = nombre

    def __repr__(self):
        return f"Almacen({self.nombre}, codigo={self.codigo})"


class Coleccion:
    def __init__(self, nombre: str, descripcion: str = ""):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetos: List[Objeto] = []

    def add_objeto(self, obj: "Objeto"):
        if obj not in self.objetos:
            self.objetos.append(obj)
            if self not in obj.colecciones:
                obj.colecciones.append(self)

    def remove_objeto(self, obj: "Objeto"):
        if obj in self.objetos:
            self.objetos.remove(obj)
            if self in obj.colecciones:
                obj.colecciones.remove(self)

    def __repr__(self):
        return f"Coleccion({self.nombre}, objetos={len(self.objetos)})"


class ColeccionTemporal(Coleccion):
    def __init__(self, nombre: str, descripcion: str, fecha_inicio: date, fecha_fin: date):
        super().__init__(nombre, descripcion)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def vigente(self, hoy: Optional[date] = None) -> bool:
        if hoy is None:
            hoy = date.today()
        return self.fecha_inicio <= hoy <= self.fecha_fin

    def __repr__(self):
        return f"ColeccionTemporal({self.nombre}, {self.fecha_inicio}–{self.fecha_fin}, objetos={len(self.objetos)})"


class Restauracion:
    def __init__(self, fecha: date, descripcion: str, tecnica: str):
        self.fecha = fecha
        self.descripcion = descripcion
        self.tecnica = tecnica
        self.objetos: List[Objeto] = []

    def añadir_objeto(self, obj: "Objeto"):
        if obj not in self.objetos:
            self.objetos.append(obj)
        if self not in obj.restauraciones:
            obj.restauraciones.append(self)
            obj.estado = EstadoObjeto.EN_RESTAURACION

    def finalizar(self):
        for o in self.objetos:
            o.estado = EstadoObjeto.RESTAURADO

    def __repr__(self):
        return f"Restauracion(fecha={self.fecha}, tecnica={self.tecnica}, objetos={len(self.objetos)})"


class Objeto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        autor: str,
        fecha_creacion: date,
        descripcion: str,
        origen: Origen,
        estado: EstadoObjeto,
        tematica: Tematica
    ):
        self.codigo = str(codigo)
        self.nombre = nombre
        self.autor = autor
        self.fecha_creacion = fecha_creacion
        self.descripcion = descripcion
        self.origen = origen
        self.estado = estado
        self.tematica = tematica
        self.ubicacion: Optional[Ubicacion] = None
        self.colecciones: List[Coleccion] = []
        self.restauraciones: List[Restauracion] = []

    def mover_a(self, destino: Ubicacion):
        if self.ubicacion is destino:
            return
        if self.ubicacion:
            self.ubicacion.remove_objeto(self)
        destino.add_objeto(self)

    def agregar_a_coleccion(self, coleccion: Coleccion):
        coleccion.add_objeto(self)

    def solicitar_restauracion(self, restauracion: Restauracion):
        restauracion.añadir_objeto(self)

    def __repr__(self):
        ubi = self.ubicacion.codigo if self.ubicacion else "sin ubicacion"
        return (f"Objeto(codigo={self.codigo}, nombre={self.nombre}, autor={self.autor}, "
                f"ubicacion={ubi}, estado={self.estado.value}, tematica={self.tematica.value})")