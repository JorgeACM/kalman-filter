# Filtro de Kalman
#
# $s(n)=as(n-1)+u(n)$

# $s(n)$ = realización del proceso Gauss-Marcov <br>
# $u(n)$ = Ruido< <br>
# $a = constante del proceso <br>

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# generar una realización del proceso aleatorio
# un modelo Gauss-Marcov
N = 30  # tamaño de la señal
a = 0.5  # valor de la cte del proceso
sigma_u = 1  # varianza del proceso

s = np.zeros(N)  # Inicializar la señal

# construir la señal
for n in np.arange(1, N):
    s[n] = a*s[n-1]+np.random.randn(1)*sigma_u

#plt.plot(s, label='realización del proceso')
# plt.legend()
# plt.show()

# generar la señal con ruido a partir de la realización
sigma_n = 0.7
sr = np.zeros(N)
# agregar ruido
for n in np.arange(1, N):
    sr[n] = s[n]+np.random.randn(1)*sigma_n

plt.plot(s, '--', label='realización del proceso')
plt.plot(sr, label='señal con ruido')
plt.legend()
plt.show()
