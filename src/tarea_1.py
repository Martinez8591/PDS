import numpy as np
from scipy.signal import sawtooth, square
from src.utils.grafica import continuous_plotter, discrete_plotter, combined_plotter

def signal_sine():

    frequency = 2
    amplitude = 1
    number_of_points = 10000
    time_initial = -1
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    x1_t = amplitude * np.sin(2 * np.pi * frequency * time)

    fs = 25
    ts = 1 / fs
    n = np.arange(time_initial, time_final, ts)
    x1_n = amplitude * np.sin(2 * np.pi * frequency * n)

    combined_plotter(
        time, x1_t,
        n, x1_n,
        'Senoidal Continua y Discreta',
        'Senoidal',
        'Tiempo [s]', 'Amplitud'
    )

def signal_exp():
    number_of_points = 10000
    time_initial = -1
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    u_t = np.where(time >= 0, 1, 0)
    x2_t = np.exp(-2 * time) * u_t


    fs = 25
    ts = 1 / fs
    n = np.arange(time_initial, time_final, ts)
    u_t = np.where( n >= 0, 1, 0)
    x2_n = np.exp(-2 * n) * u_t

    combined_plotter(
        time, x2_t,
        n, x2_n,
        'Exponencial Continua y Discreta',
        'Exponencial',
        'Tiempo [s]', 'Amplitud'
    )

def signal_sawtooth():
    global time, x3_t
    number_of_points = 10000
    time_initial = -1
    time_final = 5
    frequency = 2
    time = np.linspace(time_initial, time_final, number_of_points)
    x3_t = sawtooth(2 * np.pi * frequency * time)


    fs = 25
    ts = 1 / fs
    n = np.arange(time_initial, time_final, ts)
    x3_n = sawtooth(2 * np.pi * frequency * n)


    combined_plotter(
        time, x3_t,
        n, x3_n,
        'Rectangular Continua y Discreta',
        'Rectangular',
        'Tiempo [s]', 'Amplitud'
    )

def signal_square():
    global time, x4_t
    number_of_points = 10000
    frequency = 2
    time_initial = -1
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    x4_t = square(2 * np.pi * frequency * time)


    fs = 25
    ts = 1 / fs
    n = np.arange(time_initial, time_final, ts)
    x4_n = square(2 * np.pi * frequency * n)

    combined_plotter(
        time, x4_t,
        n, x4_n,
        'Rectangular Continua y Discreta',
        'Rectangular',
        'Tiempo [s]', 'Amplitud'
    )
