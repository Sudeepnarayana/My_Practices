import sqlite3
from datetime import datetime

# Connect to SQLite database (this will create the db file if it doesn't exist)
def connect_db():
    return sqlite3.connect('covid19.db')

# Function to create the database tables (if they don't exist)
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Patients (
        Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Age INTEGER NOT NULL,
        Gender TEXT,
        Symptom TEXT,
        Test_Result TEXT,
        Date_Of_Test DATE
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Hospitals (
        Hospital_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Hospital_Name TEXT NOT NULL,
        Location TEXT NOT NULL,
        Beds_Available INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Cases (
        Case_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Patient_ID INTEGER,
        Hospital_ID INTEGER,
        Date_Admitted DATE,
        Outcome TEXT,
        FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID),
        FOREIGN KEY (Hospital_ID) REFERENCES Hospitals(Hospital_ID)
    )''')

    conn.commit()
    conn.close()

# Function to insert a new patient record
def add_patient(name, age, gender, symptom, test_result):
    conn = connect_db()
    cursor = conn.cursor()

    date_of_test = datetime.now().strftime('%Y-%m-%d')
    cursor.execute('''
        INSERT INTO Patients (Name, Age, Gender, Symptom, Test_Result, Date_Of_Test)
        VALUES (?, ?, ?, ?, ?, ?)''', (name, age, gender, symptom, test_result, date_of_test))

    conn.commit()
    conn.close()

# Function to retrieve all patients' data from the database
def get_all_patients():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''SELECT Patient_ID, Name, Age, Gender, Symptom, Test_Result, Date_Of_Test FROM Patients''')
    patients = cursor.fetchall()
    
    conn.close()
    return patients
