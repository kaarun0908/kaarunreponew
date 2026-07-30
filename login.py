login 

import customtkinter as ctk
from tkinter import messagebox
import data

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


def login():

    app = ctk.CTk()

    app.title("Hospital Management System")

    app.geometry("900x550")

    app.resizable(False, False)

    # Left Side
    left = ctk.CTkFrame(app,
                        width=350,
                        fg_color="#6EB7F7",
                        corner_radius=0)

    left.pack(side="left", fill="both")

    title = ctk.CTkLabel(left,
                         text="🏥\nHospital\nManagement\nSystem",
                         font=("Arial", 28, "bold"),
                         text_color="white")

    title.place(relx=0.5, rely=0.35, anchor="center")

    # Right Side

    right = ctk.CTkFrame(app,
                         fg_color="white")

    right.pack(side="right",
               expand=True,
               fill="both")

    heading = ctk.CTkLabel(right,
                           text="Welcome Back",
                           font=("Arial", 30, "bold"),
                           text_color="#1565C0")

    heading.pack(pady=(70, 10))

    sub = ctk.CTkLabel(right,
                       text="Login to Continue",
                       font=("Arial", 15))

    sub.pack()

    username = ctk.CTkEntry(right,
                            width=280,
                            height=40,
                            placeholder_text="Username")

    username.pack(pady=25)

    password = ctk.CTkEntry(right,
                            width=280,
                            height=40,
                            placeholder_text="Password",
                            show="*")

    password.pack()

    def verify():

        user = username.get()

        pwd = password.get()

        if user in data.USERS and data.USERS[user] == pwd:

            messagebox.showinfo("Success",
                                "Login Successful")

            app.destroy()

            import patient

            patient.patient_window()

        else:

            messagebox.showerror("Error",
                                 "Invalid Username or Password")

    login_btn = ctk.CTkButton(right,
                              text="Login",
                              width=280,
                              height=42,
                              command=verify)

    login_btn.pack(pady=30)

    exit_btn = ctk.CTkButton(right,
                             text="Exit",
                             width=280,
                             height=42,
                             fg_color="red",
                             hover_color="#B71C1C",
                             command=app.destroy)

    exit_btn.pack()

    app.mainloop()



