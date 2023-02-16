import tkinter as tk

def calcola_media():
    num_voti = int(num_voti_entry.get())
    voti = []
    for i in range(num_voti):
        voto = int(input("Inserisci il voto: "))
        voti.append(voto)
    
    media = sum(voti) / num_voti
    risultato_label.config(text=f"La media dei voti è: {media:.2f}")

root = tk.Tk()
root.title("Calcolatore di media voti")

num_voti_label = tk.Label(root, text="Numero di voti:")
num_voti_entry = tk.Entry(root)
calcola_button = tk.Button(root, text="Calcola media", command=calcola_media)
risultato_label = tk.Label(root, text="")

num_voti_label.grid(row=0, column=0)
num_voti_entry.grid(row=0, column=1)
calcola_button.grid(row=1, column=0, columnspan=2, pady=10)
risultato_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
