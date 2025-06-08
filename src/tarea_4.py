import numpy as np
from src.utils.grafica import continuous_step

def dac_bits(des_bits):
    vfs = 5
    niveles = 2 ** int(des_bits)
    paso = vfs / (niveles - 1)   # Cambié aquí para que el paso sea correcto
    resolucion = (1 / (niveles - 1)) * 100
    entradas = np.arange(0, niveles)
    salida = entradas * paso

    print(f"Número de niveles: {niveles}")
    print(f"Tamaño del paso (V): {paso:.4f}")
    print(f"Resolución porcentual: {resolucion:.4f}%")
    print(f"Salida máxima real: {max(salida):.4f} V")  # Para verificar

    continuous_step(
        entradas, salida,
        f'DAC con {int(des_bits)} bits', 'Salida',
        'Entrada digital', 'Voltaje de salida [V]'
    )
