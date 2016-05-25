import numpy as juego


def main():
    print("Aplicación de la Ing. Civil")

    palabras = juego.array(["AUTOVIAS", "PUENTES", "PRESAS", "DIQUES", "ZAPATAS", "CARRETERAS"])
    crucigrama = juego.array([["C", "A", "R", "R", "E", "T", "E", "R", "A", "S"],
                              ["A", "U", "O", "P", "P", "B", "U", "O", "L", "P"],
                              ["U", "U", "O", "L", "U", "R", "U", "O", "L", "T"],
                              ["T", "D", "G", "D", "T", "E", "E", "E", "S", "E"],
                              ["O", "D", "I", "D", "O", "Q", "N", "S", "S", "S"],
                              ["V", "O", "I", "Q", "V", "Q", "U", "T", "A", "A"],
                              ["I", "O", "G", "Q", "U", "Q", "U", "E", "E", "S"],
                              ["A", "S", "R", "D", "U", "E", "U", "E", "S", "S"],
                              ["S", "O", "G", "D", "S", "E", "S", "E", "S", "K"],
                              ["T", "O", "Z", "A", "P", "A", "T", "A", "S", "K"]])

    palabras_encontradas = []
    seguir_jugando = 1

    while seguir_jugando == 1 and len(palabras_encontradas) != len(palabras):
        palabra = ""

        print("\nPalabras a encontrar:", palabras)

        print("\n", crucigrama, "\n")

        x_inicial = int(input("Ingrese la coordenada x inicial: "))
        y_inicial = int(input("Ingrese la coordenada y inicial: "))
        x_final = int(input("Ingrese la coordenada x final: "))
        y_final = int(input("Ingrese la coordenada y final: "))

        print()

        if x_inicial == x_final:
            for x in range(y_inicial, y_final + 1, 1):
                palabra += crucigrama[x_inicial][x]
        elif y_inicial == y_final:
            for x in range(x_inicial, x_final + 1, 1):
                palabra += crucigrama[x][y_inicial]
        elif (x_inicial - x_final) == (y_inicial - y_final):
            y = y_inicial
            for x in range(x_inicial, x_final + 1, 1):
                palabra += crucigrama[x][y]
                y += 1

        print("Palabra seleccionada:", palabra)

        if (palabra in palabras) and (palabra not in palabras_encontradas):
            palabras_encontradas.append(palabra)

            if x_inicial == x_final and y_inicial != y_final:
                for x in range(y_inicial, y_final + 1, 1):
                    crucigrama[x_inicial][x] = str(crucigrama[x_inicial][x]).lower()
            elif y_inicial == y_final and x_inicial != x_final:
                for x in range(x_inicial, x_final + 1, 1):
                    crucigrama[x][y_inicial] = str(crucigrama[x][y_inicial]).lower()
            elif (x_inicial - x_final) == (y_inicial - y_final):
                y = y_inicial
                for x in range(x_inicial, x_final + 1, 1):
                    crucigrama[x][y] = str(crucigrama[x][y]).lower()
                    y += 1

            print("Has encontrado", palabra, "palabras encontradas", len(palabras_encontradas))
        else:
            print("No has encontrado palabras")

        print()

        if len(palabras_encontradas) != len(palabras):
            seguir_jugando = int(input("¿Deseas seguir jugando? (1 = si : 0 = no): "))

            while seguir_jugando != 0 and seguir_jugando != 1:
                seguir_jugando = int(input("Entrada invalida, ¿Deseas seguir jugando? (1 = si : 0 = no): "))
        else:
            print("¡Has Ganado!")

        print("-----------------------------------------------")

    return 0


main()
