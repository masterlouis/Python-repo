import matplotlib.pyplot as plt

#dati del grafico

x = [1, 2, 3, 4, 5]
y1 = [12, 1, 34, 85, 47]
y2 = [34, 22, 69, 27, 99]


#crea il grafico a linee
plt.plot(x,y1, label="italiani", color="red", linewidth=5, linestyle="--", marker="o")
plt.plot(x,y2, label="francesi")


plt.title("grafico a linee semplice")

plt.xlabel("Valori di x")
plt.ylabel("valori di y")
plt.grid() #serve per creare la griglia
plt.legend()

plt.show()