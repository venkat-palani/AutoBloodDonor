# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox
# from THREE_inserting_donners_information_to_database import doner
# import mysql.connector
# from THREE_doners_registration_portal_info import Info
# import threading
#
#
# class donners_registration_tkscreen():
#     def __init__(self):
#         self.list = []
#
#         def clear():
#             self.blood_group.set('')
#             self.cities.set('')
#             self.donners_name.delete(0, END)
#             self.d_number.delete(0, END)
#             self.date_of_blood_donnated_text.delete(0, END)
#             self.blood_group.set("Select The Blood Group")
#             self.cities.set("Select The City")
#
#         def commandd():
#             a = self.donners_name.get()
#             b = self.blood_group.get()
#             c = self.d_number.get()
#             d = self.cities.get()
#             e = self.date_of_blood_donnated_text.get()
#             if e == "":
#                 e = None
#             if a != "" and b != "Select The Blood Group" and c != "" and d != "Select The City":
#                 if len(c) == 10:
#                     try:
#                         record = [a, b, c, d]
#                         if record not in self.list:
#                             conn = mysql.connector.connect(
#                                 user='root', password='VENKAT21o22oo2@', host='localhost', database='donners_list')
#                             cursor = conn.cursor()
#                             sql = '''SELECT count(*) from doners_details'''
#                             cursor.execute(sql)
#                             result = cursor.fetchone()
#                             aa = result[0]
#                             print(aa)
#                             conn.close()
#
#                             self.list.append(record)
#                             print(self.list)
#                             doner(aa + 1, a, b, c, e, d)
#                             info_mation = Info(a, aa + 1, c)
#                             info_mation.whatsapp()
#                             answer = messagebox.showinfo("INFO", f"Successfully Registration\nUnique Donner Id Shared "
#                                                                  f"in Whatsapp")
#
#                             Label(text=answer, font=('Arial 20 bold')).pack()
#                         else:
#                             try:
#                                 answer = messagebox.showinfo("INFO", "Duplicate Record")
#                                 Label(text=answer, font=('Arial 20 bold')).pack()
#                             except:
#                                 pass
#                     except:
#                         pass
#                 else:
#                     try:
#                         answer = messagebox.showinfo("INFO", "Please Enter The Valid Contact Number")
#                         Label(text=answer, font=('Arial 20 bold')).pack()
#                     except:
#                         pass
#
#             else:
#                 try:
#                     answer = messagebox.showinfo("INFO", "Please Enter All Field")
#                     Label(text=answer, font=('Arial 20 bold')).pack()
#                 except:
#                     pass
#
#         self.screen = Tk()
#         self.screen.maxsize(950, 950)
#         self.screen.minsize(950, 950)
#         self.screen.title(string="Auto Contact Blood Donors")
#
#         self.info = Label(text="Welcome to the Donors Registration Portal")
#         self.info.grid(column=0, row=0)
#         self.info.config(font=("Arial", 22, "bold"))
#         self.info.config(pady=20, padx=180)
#
#         self.donners_name_label = Label(text="Enter the Donor's Name Below :")
#         self.donners_name_label.grid(column=0, row=1)
#         self.donners_name_label.config(font=("Arial", 15, "bold"))
#         self.donners_name_label.config(pady=10)
#
#         self.donners_name = Entry(width=50)
#         self.donners_name.grid(column=0, row=2)
#         self.donners_name.focus()
#
#         self.donners_blood_group_label = Label(text="Select the Donor's Blood Group:")
#         self.donners_blood_group_label.grid(column=0, row=3)
#         self.donners_blood_group_label.config(pady=20)
#         self.donners_blood_group_label.config(font=("Arial", 15, "bold"))
#
#         self.blood_group = StringVar(self.screen)
#         self.blood_group.set("Select The Blood Group")
#         self.list_of_blood_group = OptionMenu(self.screen, self.blood_group, "a positive", "a negative", "b positive",
#                                               "b negative"
#                                               , "ab positive", "ab negative", "o positive", "o negative")
#         self.list_of_blood_group.grid(column=0, row=4)
#         self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)
#
#         self.donners_mobile_number = Label(text="Enter the  Donor's Contact Number:")
#         self.donners_mobile_number.grid(column=0, row=5)
#         self.donners_mobile_number.config(pady=20)
#         self.donners_mobile_number.config(font=("Arial", 15, "bold"))
#
#         self.d_number = Entry(width=50)
#         self.d_number.grid(column=0, row=6)
#
#         self.donners_locatiom = Label(text="Select the Donor's Location\City:")
#         self.donners_locatiom.grid(column=0, row=7)
#         self.donners_locatiom.config(pady=20)
#         self.donners_locatiom.config(font=("Arial", 15, "bold"))
#
#         self.cities = StringVar(self.screen)
#         self.cities.set("Select The City")
#         self.list_of_location = OptionMenu(self.screen, self.cities, "coimbatore", "chennai", "hosur", "madurai",
#                                            "karaikudi", "karur",
#                                            "trichy", "namakal")
#         self.list_of_location.grid(column=0, row=8)
#         self.list_of_location.config(height=2, highlightbackground="red", highlightcolor="blue", highlightthickness=10)
#
#         self.date_of_blood_donated = Label(text=f"Date of last blood donated (optional)\nyear-month-date\n(2020-9-21)")
#         self.date_of_blood_donated.grid(column=0, row=9)
#         self.date_of_blood_donated.config(pady=20)
#         self.date_of_blood_donated.config(font=("Arial", 15, "bold"))
#
#         self.date_of_blood_donnated_text = Entry(width=50)
#         self.date_of_blood_donnated_text.grid(column=0, row=10)
#
#         # self.button = Button(self.screen,command=threading.Thread(target=commandd).start)
#
#         self.button = Button(command=commandd)
#         self.button.config(text="Register")
#         self.button.place(x=300, y=689)
#         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#         self.clear = Button(command=clear, width=8)
#         self.clear.config(text="Clear")
#         self.clear.place(x=500, y=689)
#         self.clear.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#         self.image = Image.open("2.jpg")
#         self.resise_image = self.image.resize((270, 400))
#         self.img = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label = Label(image=self.img)
#         self.image_label.place(x=15, y=150)
#
#         self.image1 = Image.open("2.jpg")
#         self.resise_image1 = self.image.resize((270, 400))
#         self.img1 = ImageTk.PhotoImage(self.resise_image)
#
#         self.image_label1 = Label(image=self.img1)
#         self.image_label1.place(x=660, y=150)
#
#         self.image2 = Image.open("2.jpg")
#         self.resise_image2 = self.image2.resize((70, 80))
#         self.img2 = ImageTk.PhotoImage(self.resise_image2)
#
#         self.image_label2 = Label(image=self.img2)
#         self.image_label2.place(x=300, y=415)
#
#         self.screen.mainloop()
#
# # v = donners_registration_tkscreen()


############################################################################################################################



from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from THREE_inserting_donners_information_to_database import doner
import mysql.connector
from THREE_doners_registration_portal_info import Info
import threading
import tkinter
import customtkinter


class donners_registration_tkscreen():
    def __init__(self):
        self.list = []

        def clear():
            self.blood_group.set('')
            self.cities.set('')
            self.donners_name.delete(0, END)
            self.d_number.delete(0, END)
            self.date_of_blood_donnated_text.delete(0, END)
            self.blood_group.set("Select The Blood Group")
            self.cities.set("Select The City")

        def commandd():
            a = self.donners_name.get()
            b = self.blood_group.get()
            c = self.d_number.get()
            d = self.cities.get()
            e = self.date_of_blood_donnated_text.get()
            if e == "":
                e = None
            if a != "" and b != "Select The Blood Group" and c != "" and d != "Select The City":
                if len(c) == 10:
                    try:
                        record = [a, b, c, d]
                        if record not in self.list:
                            conn = mysql.connector.connect(
                                user='root', password='VENKAT21o22oo2@', host='localhost', database='donners_list')
                            cursor = conn.cursor()
                            sql = '''SELECT count(*) from doners_details'''
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            aa = result[0]
                            print(aa)
                            conn.close()

                            self.list.append(record)
                            print(self.list)
                            doner(aa + 1, a, b, c, e, d)
                            info_mation = Info(a, aa + 1, c)
                            info_mation.whatsapp()
                            answer = messagebox.showinfo("INFO", f"Successfully Registered Donor Id Shared")

                            Label(text=answer, font=('Arial 20 bold')).pack()
                        else:
                            try:
                                answer = messagebox.showinfo("INFO", "Duplicate Record")
                                Label(text=answer, font=('Arial 20 bold')).pack()
                            except:
                                pass
                    except:
                        pass
                else:
                    try:
                        answer = messagebox.showinfo("INFO", "Please Enter The Valid Contact Number")
                        Label(text=answer, font=('Arial 20 bold')).pack()
                    except:
                        pass

            else:
                try:
                    answer = messagebox.showinfo("INFO", "Please Enter All Field")
                    Label(text=answer, font=('Arial 20 bold')).pack()
                except:
                    pass

        self.screen = customtkinter.CTk()
        width, height = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
        self.screen.geometry('%dx%d+0+0' % (width, height))

        self.screen.title(string="Registration")

        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
        l1 = customtkinter.CTkLabel(master=self.screen, image=img1)
        l1.pack()

        frame = customtkinter.CTkFrame(master=l1, width=500, height=470, corner_radius=15)
        # frame.place(x=40, y=160)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.ll2 = customtkinter.CTkLabel(master=frame, text="Registration", font=('Century Gothic', 20))
        self.ll2.place(x=50, y=35)


        self.donners_name_label = customtkinter.CTkLabel(master=frame,text="Donor's Name",font=('Century Gothic', 15))
        self.donners_name_label.place(x=50,y=90)

        self.donners_name = customtkinter.CTkEntry(master=frame,width=200)
        self.donners_name.place(x=250,y=90)
        self.donners_name.focus()

        self.donners_blood_group_label = customtkinter.CTkLabel(master=frame,text="Donor's Blood Group",font=('Century Gothic', 15))
        self.donners_blood_group_label.place(x=50,y=140)



        self.blood_group = customtkinter.CTkOptionMenu(master=frame,
                                                               values=["a positive", "a negative", "b positive",
                                                                       "b negative"
                                                                   , "ab positive", "ab negative", "o positive",
                                                                       "o negative"], width=200)
        self.blood_group.place(x=250, y=140)
        self.blood_group.set('Blood Group')


        self.donners_mobile_number = customtkinter.CTkLabel(master=frame,text="Donor's Contact Number",font=('Century Gothic',15))
        self.donners_mobile_number.place(x=50,y=190)


        self.d_number = customtkinter.CTkEntry(master=frame,width=200)
        self.d_number.place(x=250,y=190)

        self.donners_locatiom = customtkinter.CTkLabel(master=frame,text="Location\City",font=('Century Gothic',15))
        self.donners_locatiom.place(x=50,y=240)



        self.cities = customtkinter.CTkOptionMenu(master=frame,
                                                            values=["coimbatore", "chennai", "hosur", "madurai",
                                                                    "karaikudi", "karur",
                                                                    "trichy", "namakal"], width=200)
        self.cities.place(x=250, y=240)
        self.cities.set('Location')


        self.date_of_blood_donated = customtkinter.CTkLabel(master=frame,text="Last Blood Donated Date",font=('Century Gothic',15))
        self.date_of_blood_donated.place(x=50,y=290)


        self.date_of_blood_donnated_text = customtkinter.CTkEntry(master=frame,width=200)
        self.date_of_blood_donnated_text.place(x=250,y=290)



        self.button = customtkinter.CTkButton(master=frame, width=220, text="Register",
                                              command=commandd, corner_radius=10,
                                              font=('Bold', 20))
        self.button.place(x=150, y=350)


        self.clear = customtkinter.CTkButton(master=frame,width=220,text="Clear",command=clear,corner_radius=10,font=('Bold',20))

        self.clear.place(x=150, y=400)




        self.screen.mainloop()
