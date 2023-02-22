import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text="BMI: {:.2f}".format(bmi))

    if bmi < 18.5:
        status = "sottopeso"
        range_label.config(text="Range: < 18.5")
    elif bmi < 25:
        status = "normopeso"
        range_label.config(text="Range: 18.5 - 24.9")
    else:
        status = "sovrappeso"
        range_label.config(text="Range: > 25")

    status_label.config(text="Stato del peso: {}".format(status))

root = tk.Tk()
root.title("BMI Calculator")

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=0, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=1, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=0)

bmi_label = tk.Label(root, text="BMI:")
bmi_label.grid(row=2, column=1)

status_label = tk.Label(root, text="Stato del peso:")
status_label.grid(row=3, column=0)

range_label = tk.Label(root, text="Range:")
range_label.grid(row=3, column=1)

root.mainloop()
