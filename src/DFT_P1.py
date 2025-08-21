import numpy as np
from src.utils.grafica import continuous_plotter, discrete_plotter


def dft_signal():

    fm = 0.5
    fc = 8.0
    m = 0.5
    fs = 64
    T = 4
    N = int(fs * T)

    t = np.linspace(0, T, 10000)
    x_t = (1 + m*np.cos(2*np.pi*fm*t)) * np.sin(2*np.pi*fc*t)
    continuous_plotter(t, x_t, "Señal continua", "continua", "Tiempo [s]", "Amplitud")

    n = np.arange(N)
    x_n = (1 + m*np.cos(2*np.pi*(fm/fs)*n)) * np.sin(2*np.pi*(fc/fs)*n)
    discrete_plotter(n, x_n, "Señal discreta", "discreta", "n·Ts", "Amplitud")

    X = np.fft.fft(x_n)
    k = np.arange(N)
    discrete_plotter(k, np.abs(X), "DFT (índice de frecuencia)", "dft", "k", "Amplitud")

    freqs = np.fft.fftfreq(N, 1/fs)
    discrete_plotter(freqs[:N//2], np.abs(X[:N//2])/N,
                     "Espectro de magnitud", "dft", "Frecuencia [Hz]", "Magnitud")

    delta_f = fs / N
    print(f"Resolución en frecuencia Δf = {delta_f:.4f} Hz")

    mag = np.abs(X[:N//2]) / N
    threshold = 0.1 * np.max(mag)
    peak_idx = np.where(mag > threshold)[0]
    print("Picos espectrales (f [Hz] - amplitud):")
    for i in peak_idx:
        print(f"{freqs[i]:.2f} Hz -> {mag[i]:.3f}")
