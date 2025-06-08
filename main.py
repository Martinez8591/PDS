import sys
from src.tarea_1 import signal_sine, signal_exp, signal_sawtooth, signal_square
from src.tarea_2 import understanding_freq
from src.tarea_3 import understanding_faf
from src.tarea_4 import dac_bits

def main(options):
    if options[1] == "T_1":
        signal_sine()
        signal_exp()
        signal_sawtooth()
        signal_square()

    elif options[1] == "T_2":
        if len(options) > 2:
            understanding_freq(options[2])

        else:
            print("Please give a frequency. ")
            print("Example: python main.py T_2 2")
    elif options[1] == "T_3":
        if len(options) > 4:
            freq = float(options[2])
            ampl = float(options[3])
            phase = float(options[4])
            understanding_faf(freq, ampl, phase)
        else:
            print("Please give frequency, amplitude, and phase.")
            print("Example: python main.py T_3 1 1 0")
    elif options[1] == "T_4":
        if len(options) > 2:
            dac_bits(options[2])

        else:
            print("Please give a number of bits for T_4")
            print("Example: python main.py T_4 2")
if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example (run tarea 1): python main.py T_1")
        print("Example (run tarea 2): python main.py T_2 2")
        print("Example (run tarea 3): python main.py T_3 1 1 0")
        print("Example (run tarea 4): python main.py T_4 4")