from matplotlib import pyplot as plt

plt.style.use("ggplot")

slices = [40, 20, 50, 2, 15]
labels = ["si", "no", "forse", "non so", "preferisco non dire"]
plt.pie(slices, labels=labels, wedgeprops={"edgecolor": "green"})

plt.title("nome del grafico")
plt.show()