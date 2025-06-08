import numpy as np
from src.utils.grafica import continuous_plotter


def understanding_freq(des_freq):
    initial_time = -1
    end_time = 5
    frequency = float(des_freq)
    amplitude = 1
    number_of_points = 1000
    time = np.linspace(initial_time, end_time, number_of_points)
    xt = amplitude * np.sin(2 * np.pi * frequency * time)
    continuous_plotter(time, xt,
    f'Señal continua con frecuencia = {frequency} Hz', "señal sin ",
    'Tiempo [s]', 'Amplitud')