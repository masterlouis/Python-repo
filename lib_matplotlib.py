import numpy as np
from matplotlib import pyplot as plt

plt.style.use("ggplot")
indexs = np.arange(6)
width = 0.3

x = [25,26,27,28,29,30]
y1 = [100,90,120,140,120,150]
y2 = [90, 91, 92, 93, 94, 95]

plt.bar(indexs+width ,y1, label="francesi", width=width, color="red")
plt.bar(indexs,y2, label="italiani", width=width, color="green")
plt.title("Nome del Grafico")
plt.xlabel("età")
plt.ylabel("valori")
plt.legend()

plt.show()