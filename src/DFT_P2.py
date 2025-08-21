import numpy as np
from src.utils.grafica import continuous_plotter, discrete_plotter

def dft_p2():
    fs = 256
    T = 6
    N = fs * T
    t = np.arange(N) / fs

    f1 = 10
    f2 = 25
    fr = 60

    señal = 1.5*np.sin(2*np.pi*f1*t) + 0.8*np.sin(2*np.pi*f2*t)
    señal_con_ruido = señal + 0.5*np.sin(2*np.pi*fr*t)

    fft_señal = np.fft.fft(señal)[:N//2] / N
    fft_ruido = np.fft.fft(señal_con_ruido)[:N//2] / N
    freqs = np.fft.fftfreq(N, 1/fs)[:N//2]

    print(f"Resolución en frecuencia: {fs/N:.4f} Hz")

    picos_señal = np.where(np.abs(fft_señal) > 0.1*np.max(np.abs(fft_señal)))[0]
    picos_ruido = np.where(np.abs(fft_ruido) > 0.1*np.max(np.abs(fft_ruido)))[0]

    print("Picos señal limpia:")
    for i in picos_señal:
        print(f"{freqs[i]:.2f} Hz -> {np.abs(fft_señal[i]):.3f}")

    print("Picos señal con ruido:")
    for i in picos_ruido:
        print(f"{freqs[i]:.2f} Hz -> {np.abs(fft_ruido[i]):.3f}")

    continuous_plotter(t, señal, "Señal limpia", "x[n]", "Tiempo [s]", "Amplitud")
    discrete_plotter(freqs, np.abs(fft_señal), "DFT señal limpia", "|X(f)|", "Frecuencia [Hz]", "Magnitud")
    continuous_plotter(t, señal_con_ruido, "Señal con ruido", "x[n]+ruido", "Tiempo [s]", "Amplitud")
    discrete_plotter(freqs, np.abs(fft_ruido), "DFT señal con ruido", "|X(f)|", "Frecuencia [Hz]", "Magnitud")
