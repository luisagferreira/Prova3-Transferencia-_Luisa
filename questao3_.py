import numpy as np
import matplotlib.pyplot as plt


t=np.arange(0,150)
print(t)
T=2300-(2480.4*(np.exp(-0.10356*t))*(np.cos(1.3138)))
print(T)
array1=np.array(T)
plt.plot(T)
plt.title("Questão 2(b): x=L")
plt.xlabel("Tempo, t(s)")
plt.ylabel("Temperatura, T(K)")
plt.show()

T2=2300-(2480.4*(np.exp(-0.10356*t)))
print(T2)
array2=np.array(T2)
plt.plot(T2)
plt.title("Questão 2(b): x=0")
plt.xlabel("Tempo, t(s)")
plt.ylabel("Temperatura, T(K)")
plt.show()

