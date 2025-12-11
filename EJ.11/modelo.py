from datetime import date
from typing import Optional, List
from enums import Tecnica, SubTecnica, Material, EstadoConservacion

class Lugar:
    def __init__(self, institucion: str, ciudad: str, pais: str, titulo_lugar: Optional[str]=None):
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais
        self.titulo_lugar = titulo_lugar
        self.cuadros: List['Cuadro'] = []

    def add_cuadro(self, cuadro: 'Cuadro'):
        if cuadro not in self.cuadros:
            self.cuadros.append(cuadro)
            cuadro.ubicacion = self

    def __str__(self):
        titulo = f"{self.titulo_lugar} - " if self.titulo_lugar else ""
        cuadros = ", ".join([c.titulo_principal() for c in self.cuadros]) if self.cuadros else "—"
        return f"Lugar: {titulo}{self.institucion} ({self.ciudad}, {self.pais}) | Obras: [{cuadros}]"


class Cuadro:
    def __init__(
        self,
        cronologia: date,
        tecnica: Tecnica,
        sub_tecnica: SubTecnica,
        material: Material,
        autor: str,
        estado_conservacion: EstadoConservacion,
        titulos: Optional[List[str]] = None,
        ubicacion: Optional[Lugar] = None,
        replica_of: Optional['Cuadro'] = None
    ):
        self.titulos = titulos or []
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.sub_tecnica = sub_tecnica
        self.material = material
        self.autor = autor
        self.estado_conservacion = estado_conservacion
        self.ubicacion = None
        if ubicacion:
            ubicacion.add_cuadro(self)
        self.replica_of: Optional[Cuadro] = None
        self.replicas: List[Cuadro] = []
        if replica_of:
            self.set_replica_of(replica_of)

    def set_location(self, lugar: Lugar):
        lugar.add_cuadro(self)

    def set_replica_of(self, original: 'Cuadro'):
        # asigna la relación réplica -> original (bidireccional)
        if self.replica_of is original:
            return
        if self.replica_of:
            try:
                self.replica_of.replicas.remove(self)
            except ValueError:
                pass
        self.replica_of = original
        if self not in original.replicas:
            original.replicas.append(self)

    def add_replica(self, replica: 'Cuadro'):
        replica.set_replica_of(self)

    def add_titulo(self, titulo: str):
        if titulo not in self.titulos:
            self.titulos.append(titulo)

    def titulo_principal(self) -> str:
        return self.titulos[0] if self.titulos else "Sin título"

    def __str__(self):
        tit = ", ".join(f'"{t}"' for t in self.titulos) if self.titulos else "Sin título"
        ubic = f"{self.ubicacion.institucion}, {self.ubicacion.ciudad}, {self.ubicacion.pais}" if self.ubicacion else "No localizado"
        orig = f'"{self.replica_of.titulo_principal()}"' if self.replica_of else "—"
        return (
            f"Cuadro: {tit}\n"
            f"  Cronología: {self.cronologia.year}\n"
            f"  Autor: {self.autor}\n"
            f"  Técnica: {self.tecnica.value} (sub: {self.sub_tecnica.value})\n"
            f"  Soporte: {self.material.value}\n"
            f"  Estado: {self.estado_conservacion.value}\n"
            f"  Ubicación: {ubic}\n"
            f"  Es réplica de: {orig}\n"
        )