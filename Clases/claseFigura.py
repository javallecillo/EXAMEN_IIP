import os
import math
class claseFiguras:
    def area(self):
        figura = input("Su figura es un circulo o una esfera?: ").lower()

        if figura != "circulo" and figura != "esfera":
            input("El valor ingresado no se admite. Presione Enter para volver a intentar: ")
            self.area()

        radio = float(input("\nIngrese la medida del radio de su figura: "))

        if figura == "circulo":
            area = (2 * 3.14 * radio)

            print("El área del circulo es: ", area)

        elif figura == "esfera":
            area = (4 * 3.14 * (radio*radio))

            print("El área de la esfera es: ", area)

        input("Presione Enter para salir.")
        exit()

    def volumen(self):
        figura = input("Su figura es un circulo o una esfera?: ").lower()

        if figura != "esfera":
            input("El valor ingresado no se admite. Presione Enter para volver a intentar: ")
            self.volumen()

        else:
            radio = float(input("\nIngrese la medida del radio de la esfera: "))
            volumen = (4 * 3.14 * (radio * radio * radio)) / 3

            print("El volumen de la esfera es: ", volumen)

        input("Presione Enter para salir.")
        exit()