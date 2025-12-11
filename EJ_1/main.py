from EJ_1.circulo import Circulo
from EJ_1.cuadrado import Cuadrado
from EJ_1.elipse import Elipse
from EJ_1.rectangulo import Rectangulo

def main():
    circulo = Circulo(radio=5, color="rojo")
    cuadrado = Cuadrado(lado=4, color="azul")
    elipse = Elipse(radio_mayor=6, radio_menor=3, color="amarillo")
    rectangulo = Rectangulo(ancho=8, alto=2, color="naranja")

    print(circulo)
    print(cuadrado)
    print(elipse)
    print(rectangulo)

if __name__ == "__main__":
    main()