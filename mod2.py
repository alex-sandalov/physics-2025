import numpy as np
import matplotlib.pyplot as plt

wavelength = 500e-9
a = 20e-6
d = 100e-6
L = 1

x = np.linspace(-5e-3, 5e-3, 5000)
k = 2 * np.pi / wavelength

beta = np.pi * a * x / (wavelength * L)
I_single = (np.sinc(beta / np.pi))**2

delta = np.pi * d * x / (wavelength * L)
I_double = (np.cos(delta))**2 * I_single

plt.figure(figsize=(10,5))
plt.plot(x * 1e3, I_single, label='Одна щель')
plt.plot(x * 1e3, I_double, label='Две щели')
plt.xlabel('x (мм)')
plt.ylabel('Интенсивность (отн.)')
plt.title('Интерференционная картина (Фраунгофер)')
plt.grid()
plt.legend()
plt.show()
