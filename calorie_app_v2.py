import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

def submit_onclick():
    if unit_system.get() == "metric":
        weight = weight_entry.get()
        height = height_entry.get()
    else:
        feet = float(ft_entry.get())
        inches = float(inches_entry.get())
        height = (feet * 0.3048) + (inches * 0.0254)
        weight = float(weight_entry.get()) * 0.453592

    bmi = float(weight) / float(height) ** 2
    bmi_rounded = "{:.2f}".format(bmi)
    messagebox.showinfo("Testing!", "Your height = " + str(height) + "m" + "\n" + "Your weight = " + str(weight) + "kg" +
                        "\n" + "BMI = " + str(bmi_rounded))

# Function to update input fields based on the selected unit system
def update_input_fields():
    if unit_system.get() == "metric":
        height_lbl.configure(text="Height (m):")
        weight_lbl.configure(text="Weight (kg):")
        ft_entry.grid_forget()
        inches_entry.grid_forget()
        height_entry.grid(row=0, column=1)  # Re-add the height entry
        weight_entry.grid(row=1, column=1, padx=40, pady=10, columnspan=1)
        frame.grid_columnconfigure(4, minsize=0)
        frame.grid_columnconfigure(5, minsize=0)
    else:
        height_lbl.configure(text="Height (ft/in):")
        weight_lbl.configure(text="Weight (lb):")
        ft_entry.grid(row=0, column=2)
        inches_entry.grid(row=0, column=4)
        height_entry.grid_forget()  # Remove the height entry
        weight_entry.grid(row=1, column=1, padx=40, pady=10, columnspan=3)
        frame.grid_columnconfigure(4, minsize=20)
        frame.grid_columnconfigure(5, minsize=20)



# Set appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# Set root and dimensions
root = ctk.CTk()
root.geometry("500x380")

# Frame that encapsulates the title
title_frame = ctk.CTkFrame(root)
title_frame.pack(pady=20, padx= 40)
title_lbl = ctk.CTkLabel(title_frame, text="BMI Calculator", padx=40, pady=10 ,font=("Consolas", 42)).pack()

# Frame for selecting imperial or metric units
unit_frame = ctk.CTkFrame(root)
unit_frame.pack(pady=10)

unit_system = tk.StringVar(value="metric")

metric_radio = ctk.CTkRadioButton(unit_frame, text="Metric", variable=unit_system, value="metric", command=update_input_fields)
imperial_radio = ctk.CTkRadioButton(unit_frame, text="Imperial", variable=unit_system, value="imperial", command=update_input_fields)

metric_radio.grid(row=0, column=0)
imperial_radio.grid(row=0, column=1)

# Frame that contains the input form
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=40)

height_lbl = ctk.CTkLabel(frame, text="Height (m):", font=("Consolas", 12), padx=40, pady=10)
height_lbl.grid(row=0, column=0)
height_entry = ctk.CTkEntry(frame, width=50)
height_entry.grid(row=0,column=1)
weight_lbl = ctk.CTkLabel(frame, text="Weight (kg):", font=("Consolas", 12), padx=40, pady=10)
weight_lbl.grid(row=1, column=0)
weight_entry = ctk.CTkEntry(frame, width=50)
weight_entry.grid(row=1, column=1, padx=40, pady=10)

ft_entry = ctk.CTkEntry(frame, width=25)
inches_entry = ctk.CTkEntry(frame, width=25)

submit_btn = ctk.CTkButton(root, text="Submit", command=submit_onclick).pack()

root.mainloop()
