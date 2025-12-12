from datetime import date
from persona import (
    Persona,
    Ocupacion,
    Lugar,
    Documento,
    DocumentoTipo,
    Lectura,
    Evento,
    Visita,
    Sexo
)


def main():
    lugar_nac = Lugar("Pueblo Viejo", direccion="C/ Real 1", pais="Pais X")
    lugar_museo = Lugar("Museo Arqueo", direccion="Av. Cultura 10", pais="Pais X")

    juan = Persona("Juan", "Pérez", date(1970, 1, 1), Sexo.HOMBRE, segundo_apellido="García", titulo="Dr.", lugar_nacimiento=lugar_nac)
    maria = Persona("María", "López", date(1980, 5, 10), Sexo.MUJER)

    ocup1 = Ocupacion("Arqueólogo", desde=date(1995, 6, 1))
    ocup2 = Ocupacion("Curador", desde=date(2008, 1, 1), hasta=date(2015, 12, 31), organizacion="Museo Arqueo")
    ocup3 = Ocupacion("Investigador", desde=date(2016, 1, 1), organizacion="Universidad X")

    juan.anadir_ocupacion(ocup1)
    maria.anadir_ocupacion(ocup2)
    maria.anadir_ocupacion(ocup3)

    juan.anadir_contacto(maria, relacion="colaborador", desde=date(2010, 1, 1))

    visita1 = Visita(lugar_museo, fecha_inicio=date(2019, 6, 15), fecha_fin=date(2019, 6, 15), proposito="Conferencia")
    juan.anadir_visita(visita1)

    doc1 = Documento("Estudio sobre cerámica", DocumentoTipo.INFORME, fecha_publicacion=date(2019, 3, 10), autores=["Juan Pérez"])
    doc2 = Documento("Informe excavación 2020", DocumentoTipo.INFORME, fecha_publicacion=date(2021, 1, 30), autores=["María López"], identificador="INF-2021-01")

    lectura1 = Lectura(doc1, fecha_lectura=date(2019, 4, 1), notas="Revisión preliminar")
    juan.anadir_lectura(lectura1)

    evento1 = Evento("Simposio Arqueología 2019", fecha=date(2019, 6, 15))
    juan.participar_en(evento1)
    maria.participar_en(evento1)

    juan.publicar_documento(doc1)
    maria.publicar_documento(doc2)

    print("Personas creadas:")
    print(" ", juan)
    print(" ", maria)
    print("\nOcupaciones activas de María:", maria.ocupaciones_activas())
    print("\nContactos de Juan:")
    for c in juan.contactos:
        print(" ", c)

    print("\nLecturas de Juan:")
    for l in juan.lecturas:
        print(" ", l)

    print("\nEventos y participantes:")
    print(" ", evento1)
    for p in evento1.participantes:
        print("   ", p.nombre_completo())

    print("\nPublicaciones:")
    for p in (juan, maria):
        for doc in p.documentos_propios:
            print(" ", p.nombre_completo(), "->", doc)

    print("\nVisitas de Juan:")
    for v in juan.visitas:
        print(" ", v)

if __name__ == "__main__":
    main()