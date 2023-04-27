# import time
# from tkinter import *
# from PIL import ImageTk, Image
# from TWO_blood_donated_donners_database import heartful
# import threading
# from tkinter import messagebox
#
# from TWO_thanking_doners_info import Info
# import customtkinter
# import tkinter
#
#
# class updating_the_date_of_blood_given_donners_tkscreen():
#     def __init__(self):
#
#         def clear():
#             self.button['state'] = NORMAL
#             self.donners_serial_number.delete(0,END)
#             self.donner_blood_given_date.delete(0,END)
#
#         def commandd():
#             self.serial_number = self.donners_serial_number.get()
#             self.date_of_donation = self.donner_blood_given_date.get()
#             if self.serial_number != "" and self.date_of_donation != "":
#                 self.button['state'] = DISABLED
#                 v = heartful(self.date_of_donation, self.serial_number)
#                 print(v.serial_number, v.name, v.mobile_number)
#                 g = Info(v.name, self.date_of_donation, v.mobile_number, )
#                 g.whatsapp()
#                 try:
#                     answer = messagebox.showinfo("INFO", f"Date Updated Successfully {v.name}")
#
#                     Label(text=answer, font=('Arial 20 bold')).pack()
#                 except:
#                     pass
#             else:
#                 try:
#                     answer = messagebox.showinfo("INFO" , "Please Enter All Fields")
#
#                     Label(text=answer, font=('Arial 20 bold')).pack()
#                 except:
#                     pass
#             # time.sleep(3)
#             # exit()
#             # self.screen.destroy()
#
#         self.screen = customtkinter.CTk()
#
#         width, height = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
#         self.screen.geometry('%dx%d+0+0' % (width, height))
#         self.screen.title(string="Update Date")
#
#         img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
#         l1 = customtkinter.CTkLabel(master=self.screen, image=img1)
#         l1.pack()
#
#         frame = customtkinter.CTkFrame(master=l1, width=500, height=470, corner_radius=15)
#         # frame.place(x=40, y=160)
#         frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
#         ll2 = customtkinter.CTkLabel(master=frame, text="Update Date", font=('Century Gothic', 20))
#         ll2.place(x=50, y=35)
#
#
#
#
#         self.doners_info = customtkinter.CTkLabel(master=frame,text="Donor's Id",font=('Century Gothic', 15))
#         self.doners_info.place(x=50,y=120)
#
#
#         self.donners_serial_number = customtkinter.CTkEntry(master=frame,width=200)
#         self.donners_serial_number.place(x=250,y=120)
#         self.donners_serial_number.focus()
#
#
#
#         self.dateinfo = customtkinter.CTkLabel(master=frame,text="Date of Blood Donated",font=('Century Gothic', 15))
#         self.dateinfo.place(x=50,y=190)
#
#
#         self.hhhh = customtkinter.CTkLabel(master=frame,text="2015-7-27",font=('Century Gothic', 13))
#         self.hhhh.place(x=320,y=220)
#
#
#         self.donner_blood_given_date = customtkinter.CTkEntry(master=frame,width=200)
#         self.donner_blood_given_date.place(x=250,y=190)
#
#
#
#         self.button = customtkinter.CTkButton(master=frame, width=220, text="Update",
#                                               command=commandd, corner_radius=10,
#                                               font=('Bold', 20))
#         self.button.place(x=150, y=300)
#
#
#
#
#
#
#
#         self.button1 = customtkinter.CTkButton(master=frame, width=220, text="Clear",
#                                               command=clear, corner_radius=10,
#                                               font=('Bold', 20))
#         self.button1.place(x=150, y=350)
#
#
#         self.serial_number = self.donners_serial_number.get()
#         self.date_of_donation = self.donner_blood_given_date.get()
#
#
#         self.screen.mainloop()


######################################################################################################################################################33


import time
from tkinter import *
from PIL import ImageTk, Image
from TWO_blood_donated_donners_database import heartful
import threading
from tkinter import messagebox

from TWO_thanking_doners_info import Info
import customtkinter
import tkinter
from datetime import datetime

class updating_the_date_of_blood_given_donners_tkscreen():
    def __init__(self):

        def clear():
            self.button['state'] = NORMAL
            self.donners_serial_number.delete(0,END)
            # self.donner_blood_given_date.delete(0,END)

        def commandd():
            self.serial_number = self.donners_serial_number.get()
            # self.date_of_donation = self.donner_blood_given_date.get()
            if self.serial_number != "" :
                self.button['state'] = DISABLED
                dff=datetime.now()

                v = heartful(dff.date(), self.serial_number)
                print(v.serial_number, v.name, v.mobile_number)
                g = Info(v.name, dff.date(), v.mobile_number, )
                g.whatsapp()
                try:
                    answer = messagebox.showinfo("INFO", f"Date Updated Successfully {v.name}")

                    Label(text=answer, font=('Arial 20 bold')).pack()
                except:
                    pass
            else:
                try:
                    answer = messagebox.showinfo("INFO" , "Please Enter All Fields")

                    Label(text=answer, font=('Arial 20 bold')).pack()
                except:
                    pass
            # time.sleep(3)
            # exit()
            # self.screen.destroy()

        self.screen = customtkinter.CTk()

        width, height = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
        self.screen.geometry('%dx%d+0+0' % (width, height))
        self.screen.title(string="Update Date")

        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
        l1 = customtkinter.CTkLabel(master=self.screen, image=img1)
        l1.pack()

        frame = customtkinter.CTkFrame(master=l1, width=500, height=470, corner_radius=15)
        # frame.place(x=40, y=160)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        ll2 = customtkinter.CTkLabel(master=frame, text="Update Date", font=('Century Gothic', 23))
        ll2.place(x=50, y=35)




        self.doners_info = customtkinter.CTkLabel(master=frame,text="Donor's Id",font=('Century Gothic', 20))
        self.doners_info.place(x=50,y=150)


        self.donners_serial_number = customtkinter.CTkEntry(master=frame,width=200)
        self.donners_serial_number.place(x=250,y=150)
        self.donners_serial_number.focus()



        # self.dateinfo = customtkinter.CTkLabel(master=frame,text="Date of Blood Donated",font=('Century Gothic', 15))
        # self.dateinfo.place(x=50,y=190)
        #
        #
        # self.hhhh = customtkinter.CTkLabel(master=frame,text="2015-7-27",font=('Century Gothic', 13))
        # self.hhhh.place(x=320,y=220)
        #
        #
        # self.donner_blood_given_date = customtkinter.CTkEntry(master=frame,width=200)
        # self.donner_blood_given_date.place(x=250,y=190)



        self.button = customtkinter.CTkButton(master=frame, width=220, text="Update",
                                              command=commandd, corner_radius=10,
                                              font=('Bold', 20))
        self.button.place(x=150, y=300)







        self.button1 = customtkinter.CTkButton(master=frame, width=220, text="Clear",
                                              command=clear, corner_radius=10,
                                              font=('Bold', 20))
        self.button1.place(x=150, y=350)


        self.serial_number = self.donners_serial_number.get()
        # self.date_of_donation = self.donner_blood_given_date.get()


        self.screen.mainloop()

