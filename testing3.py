
import time
# importing required modules
import tkinter
import customtkinter
from PIL import ImageTk, Image
from admin import admin_credential
import tkinter
from tkinter import messagebox
from otp_email import mail, vvv
from whatsapp_cellular_otp import Info
import threading
import string
import random
from base import login,forgot_password

numbersss = 1
vvvvv = 0


def loginpage():
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()

    width, height = app.winfo_screenwidth(), app.winfo_screenheight()
    app.geometry('%dx%d+0+0' % (width, height))

    app.minsize(1280, 720)
    app.maxsize(1580, 920)
    app.title('Login')

    def fogot():
        userName = entry1.get()
        # usss=userName+"@gmail.com"
        if userName == "":
            messagebox.showinfo("Alert","Enter the Credential")
        else:
            fff=forgot_password(userName)
            if fff == 0:
                messagebox.showinfo("INFO","Password reset Mail Has Send")
            elif fff == 1:
                messagebox.showinfo("ALert","Enter the Correct Credential")


    def button_function():
        global vvvvv
        username = entry1.get()
        password = entry2.get()
        usernameadd=username+"@gmail.com"
        # print(usernameadd)

        if username != "" and password != "":
            ddd = login(usernameadd, password)
            if ddd == 0:
                app.destroy()
                # tkscreen()

            elif ddd == 1:

                messagebox.showinfo("Alert", "Invalid Email or Password")





        else:
            messagebox.showinfo("Alert ", "Please Provide Your Credential")

    img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
    l1 = customtkinter.CTkLabel(master=app, image=img1)

    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, width=690, height=360, corner_radius=15, fg_color=("white"))
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    image = Image.open("login.png")
    resise_image = image.resize((380, 380))
    img = ImageTk.PhotoImage(resise_image)

    image_label = customtkinter.CTkLabel(master=frame, image=img, text="")
    image_label.place(x=340, y=25)

    l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=10,
                                      font=('Bold', 20))
    button1.place(x=50, y=240)

    l3 = customtkinter.CTkButton(master=frame, text="Forget password", font=('Century Gothic', 10), corner_radius=10,
                                 width=100,command=fogot, fg_color=("white"),
                                 text_color='Black')
    l3.place(x=170, y=205)

        # Create custom button
    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=10,font=('Bold', 20))
    button1.place(x=50, y=240)
    #

    app.mainloop()


loginpage()