from math import radians
import numpy as np
from src.utils.grafica import combined_3plotter

def understanding_faf(des_freq, des_ampl, des_phase):

    frequency = float(des_freq)
    amplitude = float(des_ampl)
    number_of_points = 10000
    phase = float(radians(des_phase))
    time_initial = -1
    time_final = 5

    time = np.linspace(time_initial, time_final, number_of_points)
    x1_t = amplitude * np.sin(2 * np.pi * frequency * time + phase )

    time = np.linspace(time_initial, time_final, number_of_points)
    x2_t = 1 * np.sin(2 * np.pi * 1 * time + radians(0))

    fs = 20
    ts = 1 / fs
    time_initial = -1
    time_final = 5
    n = np.arange(time_initial, time_final, ts)
    x1_n = amplitude * np.sin(2 * np.pi * frequency * n + phase)

    print(f"Frecuencia= {frequency}Hz Amplitud= {amplitude} Fase= {phase}rad")

    combined_3plotter(
        time, x1_t,
        time, x2_t,
        n, x1_n,
        f'Frecuencia = {frequency}Hz, amplitud = {amplitude} y fase = {phase} rad  ','Señal',
        'Tiempo [s]', 'Amplitud'
    )