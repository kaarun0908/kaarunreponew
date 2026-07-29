import customtkinter as ctk

from tkinter import ttk, messagebox
from appointment import appointment_window
# ------------------------------
# Theme
# ------------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Temporary Storage
patients = []
appointments = []

def patient_window():

    app = ctk.CTk()
    app.title("Hospital Management System")
    app.geometry("1200x700")

    # ---------------- Sidebar ----------------
    sidebar = ctk.CTkFrame(app, width=220, fg_color="#1565C0")
    sidebar.pack(side="left", fill="y")

    title = ctk.CTkLabel(
        sidebar,
        text="🏥\nHospital\nManagement",
        font=("Arial", 24, "bold"),
        text_color="white"
    )
    title.pack(pady=40)

    ctk.CTkButton(
        sidebar,
        text="Patient Registration",
        width=180
    ).pack(pady=15)

    ctk.CTkButton(
    sidebar,
    text="Book Appointment",
    width=180,
    fg_color="#0D47A1",
    hover_color="#1976D2",
    command=appointment_window
).pack(pady=10)

    ctk.CTkButton(
        sidebar,
        text="Logout",
        fg_color="red",
        hover_color="#B71C1C",
        width=180,
        command=app.destroy
    ).pack(side="bottom", pady=30)

    # ---------------- Main ----------------
    main = ctk.CTkFrame(app, fg_color="white")
    main.pack(side="right", fill="both", expand=True)

    heading = ctk.CTkLabel(
        main,
        text="Patient Registration",
        font=("Arial", 28, "bold"),
        text_color="#1565C0"
    )
    heading.pack(pady=20)

    

    form = ctk.CTkFrame(main, fg_color="transparent")
    form.pack()

    # ---------------- Entries ----------------

    ctk.CTkLabel(form, text="Patient Name").grid(row=0, column=0, padx=20, pady=10)

    name = ctk.CTkEntry(form, width=250)
    name.grid(row=0, column=1)

    ctk.CTkLabel(form, text="Age").grid(row=1, column=0)

    age = ctk.CTkEntry(form, width=250)
    age.grid(row=1, column=1)

    ctk.CTkLabel(form, text="Gender").grid(row=2, column=0)

    gender = ctk.CTkComboBox(
        form,
        values=["Male", "Female", "Other"],
        width=250
    )
    gender.grid(row=2, column=1)

    ctk.CTkLabel(form, text="Phone").grid(row=3, column=0)

    phone = ctk.CTkEntry(form, width=250)
    phone.grid(row=3, column=1)

    ctk.CTkLabel(form, text="Email").grid(row=4, column=0)

    email = ctk.CTkEntry(form, width=250)
    email.grid(row=4, column=1)

    ctk.CTkLabel(form, text="Blood Group").grid(row=5, column=0)

    blood = ctk.CTkComboBox(
        form,
        values=["A+","A-","B+","B-","AB+","AB-","O+","O-"],
        width=250
    )
    blood.grid(row=5, column=1)

    ctk.CTkLabel(form, text="Address").grid(row=6, column=0)

    address = ctk.CTkEntry(form, width=250)
    address.grid(row=6, column=1)

    # ---------------- Table ----------------

    columns = ("ID","Name","Age","Gender","Phone","Blood")

    table = ttk.Treeview(main, columns=columns, show="headings", height=8)

    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center", width=120)

    table.pack(pady=20)

    # ---------------- Functions ----------------

    def register():

        patient = {

            "id": len(patients) + 1001,

            "name": name.get(),

            "age": age.get(),

            "gender": gender.get(),

            "phone": phone.get(),

            "email": email.get(),

            "blood": blood.get(),

            "address": address.get()

        }

        patients.append(patient)

        table.insert(
            "",
            "end",
            values=(
                patient["id"],
                patient["name"],
                patient["age"],
                patient["gender"],
                patient["phone"],
                patient["blood"]
            )
        )

        messagebox.showinfo(
            "Success",
            "Patient Registered Successfully!"
        )

        name.delete(0, "end")
        age.delete(0, "end")
        phone.delete(0, "end")
        email.delete(0, "end")
        address.delete(0, "end")
        gender.set("Male")
        blood.set("O+")

    def clear():

        name.delete(0, "end")
        age.delete(0, "end")
        phone.delete(0, "end")
        email.delete(0, "end")
        address.delete(0, "end")

    # ---------------- Buttons ----------------

    btn_frame = ctk.CTkFrame(main, fg_color="transparent")
    btn_frame.pack()

    ctk.CTkButton(
        btn_frame,
        text="Register",
        width=140,
        fg_color="#1976D2",
        command=register
    ).grid(row=0, column=0, padx=10)

    ctk.CTkButton(
        btn_frame,
        text="Clear",
        width=140,
        fg_color="orange",
        command=clear
    ).grid(row=0, column=1, padx=10)

    app.mainloop()