import sys
from src.tarea_1 import  (continuous_sine, discrete_sine, combined_sine, continuous_exp, discrete_exp, combined_exp,
                         continuous_sawtooth, discrete_sawtooth, combined_sawtooth, continuous_square, discrete_square
                         , combined_square)
import os



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_console()


def main():
    while True:
        print("\n   Bienvenido. ")
        print("\n   ____________________")
        print("\n   1.- Tarea 1")
        print("   2.- Salir")
        print("   ____________________")

        option = input("\n   Ingresa Una Opcion [1] [2]:    ")
        option = int(option)

        if option == 1:

            while True:
                clear_console()
                print("\n   selecciona señal")
                print("\n   ____________________")
                print("\n   1.- Sinusoidal continua")
                print("   2.- Sinusoidal Dicreta")
                print("   3.- Sinusoidal combinada")
                print("   4.- Exponencial Continua")
                print("   5.- Exponencial Discreta")
                print("   6.- Exponencial Combinada")
                print("   7.- Triangular Continua")
                print("   8.- Triangular Discreta")
                print("   9.- Triangular Combinada")
                print("   10.- Rectangular Continua")
                print("   11.- Rectangular Discreta")
                print("   12.- Rectangular Combinada")
                print("   13.- Regresar")
                print("   ____________________")

                homework_option = input("\n   Ingresa Una Opcion [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13]:    ")
                homework_option = int(homework_option)

                if homework_option == 1:
                    continuous_sine()

                elif homework_option == 2:
                    discrete_sine()

                elif homework_option == 3:
                    combined_sine()

                elif homework_option == 4:
                    continuous_exp()

                elif homework_option == 5:
                    discrete_exp()

                elif homework_option == 6:
                    combined_exp()

                elif homework_option == 7:
                    continuous_sawtooth()

                elif homework_option == 8:
                    discrete_sawtooth()

                elif homework_option == 9:
                    combined_sawtooth()

                elif homework_option == 10:
                    continuous_square()

                elif homework_option == 11:
                    discrete_square()

                elif homework_option == 12:
                    combined_square()

                elif homework_option == 13:
                    clear_console()
                    print("\n   Regresando...")
                    break

                else:
                    print("\n   Entrada No Valida.")

        elif option == 2:

            print("\n   Saliendo...")
            print("\n")
            break


if __name__ == "__main__":
    main()