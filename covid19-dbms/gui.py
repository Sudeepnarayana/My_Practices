import tkinter as tk
from tkinter import messagebox
from database import add_patient  # Import the add_patient function from database.py

# Function to add patient data to the database
def add_patient_data():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    symptom = entry_symptom.get()
    test_result = entry_test_result.get()

    if not name or not age or not gender or not symptom or not test_result:
        messagebox.showerror("Input Error", "All fields must be filled out!")
        return

    try:
        # Call the function from database.py to add the patient
        add_patient(name, int(age), gender, symptom, test_result)
        messagebox.showinfo("Success", "Patient added successfully!")
        clear_form()
    except Exception as e:
        messagebox.showerror("Database Error", f"Error: {e}")

# Function to clear the form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_symptom.delete(0, tk.END)
    entry_test_result.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("COVID-19 Patient Entry")

# Create labels and entry fields for the form
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Gender:").grid(row=2, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=2, column=1)

tk.Label(root, text="Symptom:").grid(row=3, column=0)
entry_symptom = tk.Entry(root)
entry_symptom.grid(row=3, column=1)

tk.Label(root, text="Test Result (Positive/Negative):").grid(row=4, column=0)
entry_test_result = tk.Entry(root)
entry_test_result.grid(row=4, column=1)

# Add button to submit data
tk.Button(root, text="Add Patient", command=add_patient_data).grid(row=5, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
