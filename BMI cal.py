import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        
        if height <= 0 or weight <= 0:
            messagebox.showerror("Error", "Height and weight must be greater than 0")
            return
        
        if unit.get() == "Metric":
            bmi = weight / (height ** 2)
        else:  # Imperial
            bmi = (weight / (height ** 2)) * 703
        
        display_bmi(bmi)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Function to display BMI and corresponding message
def display_bmi(bmi):
    if bmi <= 18.5:
        result_text = f"BMI: {bmi:.2f}\nUnderweight! Increase your caloric intake."
    elif 18.5 < bmi < 24.9:
        result_text = f"BMI: {bmi:.2f}\nHealthy Weight! Maintain a balanced diet."
    elif 25.0 <= bmi < 29.9:
        result_text = f"BMI: {bmi:.2f}\nOverweight! Do cardio daily."
    else:
        result_text = f"BMI: {bmi:.2f}\nObesity! Consult a healthcare professional."
    
    label_result.config(text=result_text)

# Setting up the GUI
root = tk.Tk()
root.title("BMI Calculator")
root.configure(background="Black")
root.geometry("450x300")

frame = tk.Frame(root,background="black")
frame.pack(padx=20, pady=20)


label_unit = tk.Label(frame, text="Select Unit:",background='Black',fg="White")
label_unit.grid(row=0, column=0, pady=5)

unit = tk.StringVar(value="Metric")
radio_metric = tk.Radiobutton(frame, text="Metric (Kg, Meters)", variable=unit, value="Metric")
radio_metric.grid(row=0, column=1, pady=5)
radio_imperial = tk.Radiobutton(frame, text="Imperial (Pound, Inches)", variable=unit, value="Imperial")
radio_imperial.grid(row=0, column=2, pady=5)

label_height = tk.Label(frame, text="Height:",bg="black",fg="White")
label_height.grid(row=1, column=0, pady=5)
entry_height = tk.Entry(frame)
entry_height.grid(row=1, column=1, columnspan=2, pady=5)

label_weight = tk.Label(frame, text="Weight:",bg="black",fg="White")
label_weight.grid(row=2, column=0, pady=5)
entry_weight = tk.Entry(frame)
entry_weight.grid(row=2, column=1, columnspan=2, pady=5)

button_calculate = tk.Button(frame, text="Calculate BMI", command=calculate_bmi,background="black",fg="White")
button_calculate.grid(row=3, column=0, columnspan=3, pady=10)

label_result = tk.Label(frame, text="Your BMI will be appear here.",background='black',fg="White")
label_result.grid(row=4, column=0, columnspan=3, pady=10)

# Running the GUI
root.mainloop()