from persona import Persona

def main():
    guillermo = Persona("Guillermo", "Windsor", "Hombre")
    kate = Persona("Kate", "Windsor", "Mujer", apellido_nacimiento="Middleton")
    carlos = Persona("Carlos", "Windsor", "Hombre")
    diana = Persona("Diana", "Windsor", "Mujer", apellido_nacimiento="Spencer")

    guillermo.casar_con(kate)
    guillermo.establecer_padres(carlos, diana)

    for p in (guillermo, kate, carlos, diana):
        print(p)

if __name__ == "__main__":
    main()