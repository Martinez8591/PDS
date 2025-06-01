Graficación de Señales Continuas y Discretas
1. Señales a graficar:
x₁(t) = sin(2π·f·t) (Señal sinusoidal de frecuencia f; recomendación utilizar f=2)
x₂(t) = e^(–2t) · u(t)* (Señal exponencial;  u(t) es la señal escalón unitario: u(t)=1 para t>=0 , u(t)=0 para t<0 )
x₃(t) = tri(t, f) ( Señal triangular periódica de frecuencia f; se recomienda utilizar f=2)
x₄(t) = sq(t, f) (Señal cuadrada de frecuencia f; se recomienda utilizar f=2)

2. Dominio de tiempo:
Selecciona t ∈ [–1, 5] s (puedes ajustarlo según la señal).

3. Gráfica de la señal continua
Usa numpy.linspace con al menos 1000 puntos para generar t.
Calcula x_cont = x(t).
Grafica x_cont como línea suave.

4. Muestreo y señal discreta
Define un periodo de muestreo adecuado (definido heurísticamente, ejemplo: Tₛ = 0.01 s ).
Genera n = np.arange(N) de modo que tₙ = n·Tₛ cubra el mismo intervalo.
Calcula x_disc = x(tₙ).
Superpone los puntos muestreados sobre la gráfica continua

Al operar main se debe de obtener las graficas continua y discreta de la señal a graficar antes de ver las graficas montadas ya que
se obtienen los datos de las dos graficas anteriores para obtener la montada
