import tkinter as tk
from tkinter import messagebox
# Function to calculate BMI0   
def calculate_bmi():
    try:   #try and except method used 
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        bmi_result_label.config(text=f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            bmi_status_label.config(text="Status: Underweight")
        elif 18.5 <= bmi < 24.9:
            bmi_status_label.config(text="Status: Normal weight")
        elif 25 <= bmi < 29.9:
            bmi_status_label.config(text="Status: Overweight")
        else:
            bmi_status_label.config(text="Status: Obesity")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")   
     
# Function to calculate BMR
def calculate_bmr():
    try:   #try and except method used 
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()

        if gender == "Male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)     #formula for Bmr of male 
        elif gender == "Female":
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)     #formula for Bmr of female 

        bmr_result_label.config(text=f"BMR: {bmr:.2f} kcal/day")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Initialize main window
root = tk.Tk()
root.title("BMI and BMR Calculator")

# Create labels and entry widgets
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

tk.Label(root, text="Age (years):").grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=10)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)

# Buttons for calculation
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Calculate BMR", command=calculate_bmr).grid(row=4, column=1, columnspan=2, pady=10)

# Labels to display results
bmi_result_label = tk.Label(root, text="BMI: ")
bmi_result_label.grid(row=5, column=0, columnspan=2, pady=10)

bmi_status_label = tk.Label(root, text="Status: ")
bmi_status_label.grid(row=6, column=0, columnspan=2, pady=10)

bmr_result_label = tk.Label(root, text="BMR: ")
bmr_result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Start the application
root.mainloop()import tkinter as tk
