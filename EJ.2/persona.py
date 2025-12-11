class Persona:
    def __init__(self, nombre, apellido, sexo, apellido_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.sexo = sexo
        self.pareja = None
        self.padre = None
        self.madre = None
        self.hijos = []

    def casar_con(self, otra):
        if self.pareja is otra:
            return
        if self.pareja:
            self.pareja.pareja = None
        self.pareja = otra
        if otra.pareja:
            otra.pareja.pareja = None
        otra.pareja = self

    def establecer_padres(self, padre=None, madre=None):
        self.padre = padre
        self.madre = madre
        if padre and self not in padre.hijos:
            padre.hijos.append(self)
        if madre and self not in madre.hijos:
            madre.hijos.append(self)

    def nombre_completo(self):
        if self.apellido_nacimiento:
            return f"{self.nombre} {self.apellido} (nac. {self.apellido_nacimiento})"
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        partes = [self.nombre_completo(), f"Sexo={self.sexo}"]
        if self.pareja:
            partes.append(f"Pareja={self.pareja.nombre} {self.pareja.apellido}")
        if self.padre:
            partes.append(f"Padre={self.padre.nombre} {self.padre.apellido}")
        if self.madre:
            partes.append(f"Madre={self.madre.nombre} {self.madre.apellido}")
        if self.hijos:
            hijos_nombres = ", ".join(h.nombre + " " + h.apellido for h in self.hijos)
            partes.append(f"Hijos=[{hijos_nombres}]")
        return ", ".join(partes)