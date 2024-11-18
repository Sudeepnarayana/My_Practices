import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database import add_patient, get_all_patients, delete_patient  # Import functions from database.py
import sqlite3

# Function to add patient data to the database
def add_patient_data():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()  # Getting selected gender from dropdown
    symptom = entry_symptom.get()
    test_result = test_result_var.get()  # Getting selected test result

    if not name or not age or not symptom:
        messagebox.showerror("Input Error", "All fields must be filled out!")
        return

    try:
        # Validate and convert age to integer
        age = int(age)
    except ValueError:
        messagebox.showerror("Input Error", "Age must be a number!")
        return

    try:
        # Call the function from database.py to add the patient
        add_patient(name, age, gender, symptom, test_result)
        messagebox.showinfo("Success", "Patient added successfully!")
        clear_form()
        # Refresh the patient data display after adding a new patient
        retrieve_patients_data()

    except Exception as e:
        messagebox.showerror("Database Error", f"Error: {e}")

# Function to clear the form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set(gender_options[0])  # Reset gender dropdown to default
    entry_symptom.delete(0, tk.END)
    test_result_var.set(test_result_options[0])  # Reset test result dropdown to default

# Function to retrieve patient data from the database and display it
def retrieve_patients_data():
    # Clear existing data in the treeview
    for row in treeview.get_children():
        treeview.delete(row)

    # Fetch all patients from the database
    patients = get_all_patients()

    # Insert the fetched data into the treeview
    for patient in patients:
        treeview.insert("", "end", values=patient)

# Function to delete a selected patient from the database
def delete_patient_data():
    selected_item = treeview.selection()  # Get the selected row in Treeview
    if not selected_item:
        messagebox.showerror("Selection Error", "Please select a patient to delete!")
        return

    # Get the Patient_ID of the selected patient from the first column of the selected row
    patient_id = treeview.item(selected_item)["values"][0]

    # Confirm the deletion
    confirmation = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete patient with ID {patient_id}?")
    if not confirmation:
        return

    # Delete the patient from the database
    try:
        delete_patient(patient_id)
        # Refresh the display after deletion
        retrieve_patients_data()
        messagebox.showinfo("Success", f"Patient with ID {patient_id} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Database Error", f"Error: {e}")

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
gender_options = ["Male", "Female", "Other"]
gender_var = tk.StringVar(root)
gender_var.set(gender_options[0])  # Default to "Male"
gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
gender_menu.grid(row=2, column=1)

tk.Label(root, text="Symptom:").grid(row=3, column=0)
entry_symptom = tk.Entry(root)
entry_symptom.grid(row=3, column=1)

tk.Label(root, text="Test Result (Positive/Negative):").grid(row=4, column=0)
test_result_options = ["Positive", "Negative"]
test_result_var = tk.StringVar(root)
test_result_var.set(test_result_options[0])  # Default to "Positive"
test_result_menu = tk.OptionMenu(root, test_result_var, *test_result_options)
test_result_menu.grid(row=4, column=1)

# Add button to submit data
tk.Button(root, text="Add Patient", command=add_patient_data).grid(row=5, column=0, columnspan=2)

# Add button to retrieve and display patient data
tk.Button(root, text="Retrieve Patients", command=retrieve_patients_data).grid(row=6, column=0, columnspan=2)

# Add button to delete the selected patient
tk.Button(root, text="Delete Patient", command=delete_patient_data).grid(row=6, column=2)

# Create a Treeview widget to display patient data in a table-like format
treeview = ttk.Treeview(root, columns=("Patient_ID", "Name", "Age", "Gender", "Symptom", "Test_Result", "Date_Of_Test"), show="headings")
treeview.grid(row=7, column=0, columnspan=3)

# Define headings for the columns
treeview.heading("Patient_ID", text="Patient ID")
treeview.heading("Name", text="Name")
treeview.heading("Age", text="Age")
treeview.heading("Gender", text="Gender")
treeview.heading("Symptom", text="Symptom")
treeview.heading("Test_Result", text="Test Result")
treeview.heading("Date_Of_Test", text="Date of Test")

# Start the Tkinter main loop
root.mainloop()
