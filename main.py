import os
from src.tarea_1 import (
    continuous_sine, discrete_sine, combined_sine,
    continuous_exp, discrete_exp, combined_exp,
    continuous_sawtooth, discrete_sawtooth, combined_sawtooth,
    continuous_square, discrete_square, combined_square
)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()
        print("\n1.- Tarea 1\n2.- Salir")
        option = input("\nOpción: ")

        if option == '1':
            while True:
                clear_console()
                print("\nSelecciona señal:")
                print("1.- Sinusoidal continua")
                print("2.- Sinusoidal discreta")
                print("3.- Sinusoidal combinada")
                print("4.- Exponencial continua")
                print("5.- Exponencial discreta")
                print("6.- Exponencial combinada")
                print("7.- Triangular continua")
                print("8.- Triangular discreta")
                print("9.- Triangular combinada")
                print("10.- Rectangular continua")
                print("11.- Rectangular discreta")
                print("12.- Rectangular combinada")
                print("13.- Regresar")

                choice = input("\nOpción: ")

                if choice == '1': continuous_sine()
                elif choice == '2': discrete_sine()
                elif choice == '3': combined_sine()
                elif choice == '4': continuous_exp()
                elif choice == '5': discrete_exp()
                elif choice == '6': combined_exp()
                elif choice == '7': continuous_sawtooth()
                elif choice == '8': discrete_sawtooth()
                elif choice == '9': combined_sawtooth()
                elif choice == '10': continuous_square()
                elif choice == '11': discrete_square()
                elif choice == '12': combined_square()
                elif choice == '13':
                    print("\nRegresando...")
                    break
                else:
                    print("\nOpción no válida.")
        elif option == '2':
            print("\nSaliendo...")
            break
        else:
            print("\nOpción no válida.")

if __name__ == "__main__":
    main()
