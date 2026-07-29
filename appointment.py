from tkinter import *
from tkinter import ttk
from tkinter import messagebox

appointments = []

doctors = [
    ("Dr. Priya", "Cardiologist", "09:00 AM - 11:00 AM"),
    ("Dr. Arun", "Neurologist", "11:00 AM - 01:00 PM"),
    ("Dr. Ravi", "Orthopedic", "02:00 PM - 04:00 PM"),
    ("Dr. Meena", "Pediatrician", "10:00 AM - 12:00 PM"),
    ("Dr. Kumar", "Dermatologist", "04:00 PM - 06:00 PM")
]

def appointment_window():

    win = Toplevel()
    win.title("Book Appointment")
    win.geometry("900x650")

    Label(
        win,
        text="BOOK APPOINTMENT",
        font=("Arial",20,"bold"),
        fg="blue"
    ).pack(pady=15)

    # ---------------- Patient Name ----------------

    Label(win,text="Patient Name",font=("Arial",12,"bold")).pack()

    patient = Entry(win,width=40,font=("Arial",11))
    patient.pack(pady=5)

    # ---------------- Doctor Selection ----------------

    Label(win,text="Select Doctor",font=("Arial",12,"bold")).pack()

    doctor = ttk.Combobox(
    win,
    values=[d[0] for d in doctors],   # Show doctor names
    width=40,
    state="readonly",
    font=("Arial", 11)
)
doctor.pack(pady=5)
doctor.current(0)