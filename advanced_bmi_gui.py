import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os

FILE_NAME = "bmi_history.txt"


def save_bmi_record(bmi):
    with open(FILE_NAME, "a") as f:
        f.write(str(bmi) + "\n")


def load_bmi_history():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return [float(line.strip()) for line in f.readlines()]


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter positive values.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {category}")

        save_bmi_record(bmi)

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")


def show_history_chart():
    history = load_bmi_history()
    if not history:
        messagebox.showinfo("No Data", "No BMI records found.")
        return

    plt.plot(history, marker="o")
    plt.title("BMI History Trend")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI Value")
    plt.grid(True)
    plt.show()


# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x350")
root.configure(bg="#f2f2f2")

title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

tk.Label(root, text="Weight (kg):", bg="#f2f2f2").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (meters):", bg="#f2f2f2").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white").pack(pady=10)

bmi_label = tk.Label(root, text="BMI: --", font=("Arial", 12), bg="#f2f2f2")
bmi_label.pack()

category_label = tk.Label(root, text="Category: --", font=("Arial", 12), bg="#f2f2f2")
category_label.pack()

tk.Button(root, text="Show History Chart", command=show_history_chart, bg="#2196F3", fg="white").pack(pady=15)

root.mainloop()

