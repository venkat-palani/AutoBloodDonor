# # # # #
# # # # # # ########################################################################################################################
# # # # # #
# # # # # #
# # # # #
# # # # #
# # # # # import time
# # # # # from tkinter import *
# # # # # from PIL import ImageTk, Image
# # # # # from tkinter import messagebox
# # # # # from ONE_donersdatabase import finallistofsuitabledoners
# # # # # from FOUR_status_update_info import Info
# # # # # from ONE_patientdatabade import Patient_datas
# # # # # import customtkinter
# # # # # import tkinter
# # # # # import  threading
# # # # #
# # # # # class status_update_tkscreen():
# # # # #     def __init__(self):
# # # # #         def commandd():
# # # # #                self.patientid = self.patient_id_entry.get()
# # # # #                if self.patientid != "Enter If Known" and self.patientid != "" :
# # # # #                    self.button["state"] = DISABLED
# # # # #                    self.p=Patient_datas(int(self.patientid))
# # # # #                    self.patient_name.insert(0,f"{self.p.patientname}")
# # # # #                    self.blood_group.set(f"{self.p.patientbloodgroup}")
# # # # #                    self.cities.set(f"{self.p.city}")
# # # # #                    self.address_text.insert(END,f"{self.p.location}")
# # # # #
# # # # #                    self.pat_name = self.p.patientname
# # # # #                    self.pat_blood_group = self.p.patientbloodgroup
# # # # #                    self.city = self.p.city
# # # # #                    self.address = self.p.location
# # # # #                    gg = finallistofsuitabledoners(self.pat_blood_group, self.city)
# # # # #                    print(gg.donersfinallist)
# # # # #
# # # # #                    for i in gg.donersfinallist:
# # # # #                        dddd = Info(self.pat_name, i[3], self.address)
# # # # #                        dddd.whatsapp()
# # # # #                        # dddd.text_message()
# # # # #                    print(self.city, self.pat_name, self.pat_blood_group, self.address)
# # # # #
# # # # #                    try:
# # # # #                        answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
# # # # #                        Label(text=answer, font=('Arial 20 bold')).pack()
# # # # #                    except:
# # # # #                        pass
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #                else:
# # # # #
# # # # #                    self.pat_name = self.patient_name.get()
# # # # #                    self.pat_blood_group = self.blood_group.get()
# # # # #                    self.city = self.cities.get()
# # # # #                    self.address = self.address_text.get()
# # # # #                    a=str(self.address).split()
# # # # #
# # # # #
# # # # #                    if self.pat_name != "" and self.pat_blood_group != "Select The Blood Group" and self.city != "Select The City" and a != []:
# # # # #                         # self.button["state"] = DISABLED
# # # # #                         self.button['state'] = DISABLED
# # # # #                         gg=finallistofsuitabledoners(self.pat_blood_group,self.city)
# # # # #                         print(gg.donersfinallist)
# # # # #
# # # # #                         for i in gg.donersfinallist:
# # # # #                                dddd=Info(self.pat_name,i[3],self.address)
# # # # #                                dddd.whatsapp()
# # # # #                                # dddd.text_message()
# # # # #                         print(self.city,self.pat_name,self.pat_blood_group,self.address)
# # # # #                         try:
# # # # #                             answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
# # # # #                             Label(text=answer, font=('Arial 20 bold')).pack()
# # # # #                         except:
# # # # #                             pass
# # # # #                    else:
# # # # #                        try:
# # # # #                            answer = messagebox.showinfo("INFO", "Please Enter All Fields")
# # # # #                            Label(text=answer, font=('Arial 20 bold')).pack()
# # # # #                        except:
# # # # #                            pass
# # # # #
# # # # #
# # # # #         self.screen_Four = customtkinter.CTk()
# # # # #         width, height = self.screen_Four.winfo_screenwidth(), self.screen_Four.winfo_screenheight()
# # # # #         self.screen_Four.geometry('%dx%d+0+0' % (width,height))
# # # # #
# # # # #
# # # # #         # self.screen_Four.maxsize(1570, 920)
# # # # #         # self.screen_Four.minsize(1270, 720)
# # # # #         self.screen_Four.title(string="Status Update Page of BloodIndiaConnect")
# # # # #
# # # # #         img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
# # # # #         l1 = customtkinter.CTkLabel(master=self.screen_Four, image=img1)
# # # # #         l1.pack()
# # # # #
# # # # #         frame = customtkinter.CTkFrame(master=l1, width=500, height=470, corner_radius=15)
# # # # #         # frame.place(x=40, y=160)
# # # # #         frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# # # # #
# # # # #         self.ll2 = customtkinter.CTkLabel(master=frame, text="Status Update", font=('Century Gothic', 20))
# # # # #         self.ll2.place(x=50, y=35)
# # # # #
# # # # #         self.patient_id = customtkinter.CTkLabel(master=frame, text="Patient id", font=('Century Gothic', 15))
# # # # #         self.patient_id.place(x=50, y=90)
# # # # #
# # # # #         def click(*args):
# # # # #             self.patient_id_entry.delete(0, 'end')
# # # # #
# # # # #         self.patient_id_entry = customtkinter.CTkEntry(master=frame, width=200)
# # # # #         self.patient_id_entry.insert(0, 'Enter If Known')
# # # # #         self.patient_id_entry.place(x=250, y=90)
# # # # #         self.patient_id_entry.bind("<Button-1>", click)
# # # # #
# # # # #
# # # # #
# # # # #         self.donners_name_label = customtkinter.CTkLabel(master=frame,text="Enter the Patient's Name",font=('Century Gothic',15))
# # # # #         self.donners_name_label.place(x=50,y=140)
# # # # #
# # # # #
# # # # #         self.patient_name = customtkinter.CTkEntry(master=frame,width=200)
# # # # #         self.patient_name.place(x=250,y=140)
# # # # #         self.patient_name.focus()
# # # # #
# # # # #         self.donners_blood_group_label = customtkinter.CTkLabel(master=frame,text="Patient's Blood Group",font=('Century Gothic',15))
# # # # #         self.donners_blood_group_label.place(x=50,y=190)
# # # # #
# # # # #
# # # # #         # self.blood_group = StringVar(self.screen_Four)
# # # # #         # self.blood_group.set("Select The Blood Group")
# # # # #         self.blood_group = customtkinter.CTkOptionMenu(master=frame,
# # # # #                                                        values=["a positive", "a negative", "b positive",
# # # # #                                               "b negative"
# # # # #                                               , "ab positive", "ab negative", "o positive", "o negative"],width=200)
# # # # #         self.blood_group.place(x=250,y=190)
# # # # #         self.blood_group.set('Blood Group')
# # # # #
# # # # #
# # # # #
# # # # #         self.donners_locatiom = customtkinter.CTkLabel(master=frame,text="Location\City",font=('Century Gothic',15))
# # # # #         self.donners_locatiom.place(x=50,y=240)
# # # # #
# # # # #
# # # # #         # self.cities = StringVar(self.screen_Four)
# # # # #         # self.cities.set("Select The City")
# # # # #         self.cities = customtkinter.CTkOptionMenu(master=frame,
# # # # #                                                   values=["coimbatore", "chennai", "hosur", "madurai",
# # # # #                                            "karaikudi", "karur",
# # # # #                                            "trichy", "namkal"],width=200)
# # # # #         self.cities.place(x=250,y=240)
# # # # #
# # # # #
# # # # #         self.addressd = customtkinter.CTkLabel(master=frame,text="Hospital Name",font=('Century Gothic',15))
# # # # #         self.addressd.place(x=50,y=290)
# # # # #
# # # # #         #
# # # # #         self.address_text = customtkinter.CTkEntry(master=frame, width=200)
# # # # #         self.address_text.place(x=250,y=290)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #         self.button = customtkinter.CTkButton(master=frame, width=220, text="Inform To Donors", command=commandd,
# # # # #                                           corner_radius=6)
# # # # #         self.button.place(x=150, y=400)
# # # # #
# # # # #
# # # # #
# # # # #         self.screen_Four.mainloop()
# # # # #
# # # # # status_update_tkscreen()
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # #
# # # # # import time
# # # # # from tkinter import *
# # # # # from PIL import ImageTk, Image
# # # # # from TWO_blood_donated_donners_database import heartful
# # # # # import threading
# # # # # from tkinter import messagebox
# # # # #
# # # # # from TWO_thanking_doners_info import Info
# # # # # import customtkinter
# # # # # import tkinter
# # # # #
# # # # #
# # # # # class updating_the_date_of_blood_given_donners_tkscreen():
# # # # #     def __init__(self):
# # # # #
# # # # #         def clear():
# # # # #             self.button['state'] = NORMAL
# # # # #             self.donners_serial_number.delete(0,END)
# # # # #             self.donner_blood_given_date.delete(0,END)
# # # # #
# # # # #         def commandd():
# # # # #             self.serial_number = self.donners_serial_number.get()
# # # # #             self.date_of_donation = self.donner_blood_given_date.get()
# # # # #             if self.serial_number != "" and self.date_of_donation != "":
# # # # #                 self.button['state'] = DISABLED
# # # # #                 v = heartful(self.date_of_donation, self.serial_number)
# # # # #                 print(v.serial_number, v.name, v.mobile_number)
# # # # #                 g = Info(v.name, self.date_of_donation, v.mobile_number, )
# # # # #                 g.whatsapp()
# # # # #                 try:
# # # # #                     answer = messagebox.showinfo("INFO", f"Date Updated Successfully {v.name}")
# # # # #
# # # # #                     Label(text=answer, font=('Arial 20 bold')).pack()
# # # # #                 except:
# # # # #                     pass
# # # # #             else:
# # # # #                 try:
# # # # #                     answer = messagebox.showinfo("INFO" , "Please Enter All Fields")
# # # # #
# # # # #                     Label(text=answer, font=('Arial 20 bold')).pack()
# # # # #                 except:
# # # # #                     pass
# # # # #             # time.sleep(3)
# # # # #             # exit()
# # # # #             # self.screen.destroy()
# # # # #
# # # # #         self.screen = customtkinter.CTk()
# # # # #
# # # # #         width, height = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
# # # # #         self.screen.geometry('%dx%d+0+0' % (width, height))
# # # # #         self.screen.title(string="Date Update Page Of BloodIndiaConnect")
# # # # #
# # # # #         img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
# # # # #         l1 = customtkinter.CTkLabel(master=self.screen, image=img1)
# # # # #         l1.pack()
# # # # #
# # # # #         frame = customtkinter.CTkFrame(master=l1, width=500, height=470, corner_radius=15)
# # # # #         # frame.place(x=40, y=160)
# # # # #         frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# # # # #
# # # # #         ll2 = customtkinter.CTkLabel(master=frame, text="Update Date", font=('Century Gothic', 20))
# # # # #         ll2.place(x=50, y=35)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #         self.doners_info = customtkinter.CTkLabel(master=frame,text="Donor's Id",font=('Century Gothic', 15))
# # # # #         self.doners_info.place(x=50,y=120)
# # # # #
# # # # #
# # # # #         self.donners_serial_number = customtkinter.CTkEntry(master=frame,width=200)
# # # # #         self.donners_serial_number.place(x=250,y=120)
# # # # #         self.donners_serial_number.focus()
# # # # #
# # # # #
# # # # #
# # # # #         self.dateinfo = customtkinter.CTkLabel(master=frame,text="Date of Blood Donated",font=('Century Gothic', 15))
# # # # #         self.dateinfo.place(x=50,y=190)
# # # # #
# # # # #
# # # # #         self.hhhh = customtkinter.CTkLabel(master=frame,text="2015-7-27",font=('Century Gothic', 13))
# # # # #         self.hhhh.place(x=320,y=220)
# # # # #
# # # # #
# # # # #         self.donner_blood_given_date = customtkinter.CTkEntry(master=frame,width=200)
# # # # #         self.donner_blood_given_date.place(x=250,y=190)
# # # # #
# # # # #
# # # # #
# # # # #         self.button = customtkinter.CTkButton(master=frame, width=220, text="Update",
# # # # #                                               command=commandd, corner_radius=10,
# # # # #                                               font=('Bold', 20))
# # # # #         self.button.place(x=150, y=300)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #         self.button1 = customtkinter.CTkButton(master=frame, width=220, text="Clear",
# # # # #                                               command=clear, corner_radius=10,
# # # # #                                               font=('Bold', 20))
# # # # #         self.button1.place(x=150, y=350)
# # # # #
# # # # #
# # # # #         self.serial_number = self.donners_serial_number.get()
# # # # #         self.date_of_donation = self.donner_blood_given_date.get()
# # # # #
# # # # #
# # # # #         self.screen.mainloop()
# # # # #
# # # # # updating_the_date_of_blood_given_donners_tkscreen()
# # # #
# # # #
# # # # ##################################################################################################################################################
# # # #
# # # #
# # # # from tkinter import *
# # # # from PIL import ImageTk, Image
# # # # from tkinter import messagebox
# # # # from THREE_inserting_donners_information_to_database import doner
# # # # import mysql.connector
# # # # from THREE_doners_registration_portal_info import Info
# # # # import threading
# # # # import tkinter
# # # # import customtkinter
# # # #
# # # #
# # # # class donners_registration_tkscreen():
# # # #     def __init__(self):
# # # #         self.list = []
# # # #
# # # #         def clear():
# # # #             self.blood_group.set('')
# # # #             self.cities.set('')
# # # #             self.donners_name.delete(0, END)
# # # #             self.d_number.delete(0, END)
# # # #             self.date_of_blood_donnated_text.delete(0, END)
# # # #             self.blood_group.set("Select The Blood Group")
# # # #             self.cities.set("Select The City")
# # # #
# # # #         def commandd():
# # # #             a = self.donners_name.get()
# # # #             b = self.blood_group.get()
# # # #             c = self.d_number.get()
# # # #             d = self.cities.get()
# # # #             e = self.date_of_blood_donnated_text.get()
# # # #             if e == "":
# # # #                 e = None
# # # #             if a != "" and b != "Select The Blood Group" and c != "" and d != "Select The City":
# # # #                 if len(c) == 10:
# # # #                     try:
# # # #                         record = [a, b, c, d]
# # # #                         if record not in self.list:
# # # #                             conn = mysql.connector.connect(
# # # #                                 user='root', password='VENKAT21o22oo2@', host='localhost', database='donners_list')
# # # #                             cursor = conn.cursor()
# # # #                             sql = '''SELECT count(*) from doners_details'''
# # # #                             cursor.execute(sql)
# # # #                             result = cursor.fetchone()
# # # #                             aa = result[0]
# # # #                             print(aa)
# # # #                             conn.close()
# # # #
# # # #                             self.list.append(record)
# # # #                             print(self.list)
# # # #                             doner(aa + 1, a, b, c, e, d)
# # # #                             info_mation = Info(a, aa + 1, c)
# # # #                             info_mation.whatsapp()
# # # #                             answer = messagebox.showinfo("INFO", f"Successfully Registered Donor Id Shared")
# # # #
# # # #                             Label(text=answer, font=('Arial 20 bold')).pack()
# # # #                         else:
# # # #                             try:
# # # #                                 answer = messagebox.showinfo("INFO", "Duplicate Record")
# # # #                                 Label(text=answer, font=('Arial 20 bold')).pack()
# # # #                             except:
# # # #                                 pass
# # # #                     except:
# # # #                         pass
# # # #                 else:
# # # #                     try:
# # # #                         answer = messagebox.showinfo("INFO", "Please Enter The Valid Contact Number")
# # # #                         Label(text=answer, font=('Arial 20 bold')).pack()
# # # #                     except:
# # # #                         pass
# # # #
# # # #             else:
# # # #                 try:
# # # #                     answer = messagebox.showinfo("INFO", "Please Enter All Field")
# # # #                     Label(text=answer, font=('Arial 20 bold')).pack()
# # # #                 except:
# # # #                     pass
# # # #
# # # #         self.screen = customtkinter.CTk()
# # # #         width, height = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
# # # #         self.screen.geometry('%dx%d+0+0' % (width, height))
# # # #
# # # #         self.screen.title(string="Registration Page Of BloodIndiaConnect")
# # # #
# # # #         img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
# # # #         l1 = customtkinter.CTkLabel(master=self.screen, image=img1)
# # # #         l1.pack()
# # # #
# # # #         frame = customtkinter.CTkFrame(master=l1, width=500, height=470, corner_radius=15)
# # # #         # frame.place(x=40, y=160)
# # # #         frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# # # #
# # # #         self.ll2 = customtkinter.CTkLabel(master=frame, text="Registration", font=('Century Gothic', 20))
# # # #         self.ll2.place(x=50, y=35)
# # # #
# # # #
# # # #         self.donners_name_label = customtkinter.CTkLabel(master=frame,text="Donor's Name",font=('Century Gothic', 15))
# # # #         self.donners_name_label.place(x=50,y=90)
# # # #
# # # #         self.donners_name = customtkinter.CTkEntry(master=frame,width=200)
# # # #         self.donners_name.place(x=250,y=90)
# # # #         self.donners_name.focus()
# # # #
# # # #         self.donners_blood_group_label = customtkinter.CTkLabel(master=frame,text="Donor's Blood Group",font=('Century Gothic', 15))
# # # #         self.donners_blood_group_label.place(x=50,y=140)
# # # #
# # # #
# # # #
# # # #         self.blood_group = customtkinter.CTkOptionMenu(master=frame,
# # # #                                                                values=["a positive", "a negative", "b positive",
# # # #                                                                        "b negative"
# # # #                                                                    , "ab positive", "ab negative", "o positive",
# # # #                                                                        "o negative"], width=200)
# # # #         self.blood_group.place(x=250, y=140)
# # # #         self.blood_group.set('Blood Group')
# # # #
# # # #
# # # #         self.donners_mobile_number = customtkinter.CTkLabel(master=frame,text="Donor's Contact Number",font=('Century Gothic',15))
# # # #         self.donners_mobile_number.place(x=50,y=190)
# # # #
# # # #
# # # #         self.d_number = customtkinter.CTkEntry(master=frame,width=200)
# # # #         self.d_number.place(x=250,y=190)
# # # #
# # # #         self.donners_locatiom = customtkinter.CTkLabel(master=frame,text="Location\City",font=('Century Gothic',15))
# # # #         self.donners_locatiom.place(x=50,y=240)
# # # #
# # # #
# # # #         # self.cities = StringVar(self.screen)
# # # #         # self.cities.set("Select The City")
# # # #         # self.list_of_location = OptionMenu(self.screen, self.cities, "coimbatore", "chennai", "hosur", "madurai",
# # # #         #                                    "karaikudi", "karur",
# # # #         #                                    "trichy", "namakal")
# # # #         # self.list_of_location.place(x=10,y=23)
# # # #         # self.list_of_location.config(height=2, highlightbackground="red", highlightcolor="blue", highlightthickness=10)
# # # #
# # # #         self.cities = customtkinter.CTkOptionMenu(master=frame,
# # # #                                                             values=["coimbatore", "chennai", "hosur", "madurai",
# # # #                                                                     "karaikudi", "karur",
# # # #                                                                     "trichy", "namakal"], width=200)
# # # #         self.cities.place(x=250, y=240)
# # # #         self.cities.set('Location')
# # # #
# # # #
# # # #         self.date_of_blood_donated = customtkinter.CTkLabel(master=frame,text="Last Blood Donated Date",font=('Century Gothic',15))
# # # #         self.date_of_blood_donated.place(x=50,y=290)
# # # #
# # # #
# # # #         self.date_of_blood_donnated_text = customtkinter.CTkEntry(master=frame,width=200)
# # # #         self.date_of_blood_donnated_text.place(x=250,y=290)
# # # #
# # # #         # self.button = Button(self.screen,command=threading.Thread(target=commandd).start)
# # # #
# # # #         # self.button = Button(command=commandd)
# # # #         # self.button.config(text="Register")
# # # #         # self.button.place(x=300, y=689)
# # # #         # self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
# # # #
# # # #         self.button = customtkinter.CTkButton(master=frame, width=220, text="Register",
# # # #                                               command=commandd, corner_radius=10,
# # # #                                               font=('Bold', 20))
# # # #         self.button.place(x=150, y=350)
# # # #
# # # #
# # # #         self.clear = customtkinter.CTkButton(master=frame,width=220,text="Clear",command=clear,corner_radius=10,font=('Bold',20))
# # # #
# # # #         self.clear.place(x=150, y=400)
# # # #
# # # #
# # # #
# # # #
# # # #         self.screen.mainloop()
# # # #
# # # #
# # # #
# # # import json
# # # x = {"abinanth":{"password":"venkat","email":"venkatesanpalaniappan21@gmail.com"},
# # #      "psg":{"password":"maha","email":"venkatesanpalaniappan21@gmail.com"}}
# # #
# # #
# # #
# # #############################################################################################################################
# # import time
# # #importing required modules
# # import tkinter
# # import customtkinter
# # from PIL import ImageTk, Image
# # from admin import admin_credential
# # import tkinter
# # from tkinter import messagebox
# # from otp_email import mail,vvv
# # from whatsapp_cellular_otp import Info
# # import threading
# # import string
# # import random
# # numbersss = 1
# # vvvvv=0
# #
# #
# #
# #
# # def loginpage():
# #     customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# #     customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
# #
# #     app = customtkinter.CTk()
# #
# #     width, height = app.winfo_screenwidth(), app.winfo_screenheight()
# #     app.geometry('%dx%d+0+0' % (width, height))
# #
# #     app.minsize(1280,720)
# #     app.maxsize(1580,920)
# #     app.title('Login Page OF BLoodIndiaConnect')
# #
# #
# #
# #
# #     def forgot():
# #
# #
# #
# #
# #          def verification():
# #              def Reset_password():
# #
# #                  def  againlogin():
# #
# #                      def afterreset():
# #
# #
# #
# #                          username = entry1.get()
# #                          password = entry2.get()
# #                          global numbersss
# #                          if username != "" and password != "":
# #                              if username in admin_credential:
# #                                  g = admin_credential[username]["password"]
# #                                  if g == password:
# #                                      app.destroy()
# #                                      # tkscreen()
# #                                  else:
# #
# #                                      messagebox.showinfo("Alert", "Incorrect Password")
# #
# #
# #                              else:
# #
# #                                  messagebox.showinfo("Alert", "Incorrect Credential")
# #                          else:
# #                              messagebox.showinfo("Alert ", "Please Provide Your Credential")
# #
# #                      l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account",
# #                                                  font=('Century Gothic', 20))
# #                      l2.place(x=50, y=45)
# #
# #                      entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
# #                      entry1.place(x=50, y=110)
# #
# #                      entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
# #                      entry2.place(x=50, y=165)
# #
# #                      againlogin.destroy()
# #
# #                      button_for_login=customtkinter.CTkButton(master=frame,text="Login",command=afterreset,corner_radius=10,font=('Bold', 20),width=220)
# #                      button_for_login.place(x=50,y=270)
# #
# #
# #                  new_password = entry111.get()
# #                  confirm_password = entry112.get()
# #
# #                  if new_password == "" or confirm_password == "":
# #                      messagebox.showinfo('Alert',"Provide New Password")
# #                  elif new_password == confirm_password:
# #
# #                      image_label.destroy()
# #
# #                      image1 = Image.open("C:\\Users\\venkatesan\\Desktop\\im\\ver.png")
# #                      resise_image1 = image1.resize((380, 380))
# #                      img1 = ImageTk.PhotoImage(resise_image1)
# #
# #                      image_label1= customtkinter.CTkLabel(master=frame, image=img1, text="")
# #                      image_label1.place(x=340, y=25)
# #
# #                      admin_credential[user_name_for_password_reset]["password"]= new_password
# #                      print(admin_credential)
# #
# #                      messagebox.showinfo('Info',f"Password Updated Successfully\n"
# #                                                 f"Close The Application and Open Again")
# #
# #                      button111.destroy()
# #
# #                      againlogin = customtkinter.CTkButton(master=frame,text="Login",command=againlogin,corner_radius=10,font=('Bold', 20))
# #                      againlogin.place(x=50 , y= 270)
# #
# #
# #                  else:
# #                      messagebox.showinfo('Alert',"Password Doesnot Match")
# #
# #
# #              email = entry11.get()
# #              whatsappp = entry12.get()
# #              celluar  = entry13.get()
# #
# #              # print(type(email),type(vvv))
# #              if email != "" and whatsappp != "" and celluar != "":
# #                     if int(email) == vvv  and int(whatsappp) == otpwm and celluar == cacheee:
# #                     # if int(email) == vvv and int(whatsappp) == otpwm:
# #
# #                         lll.destroy()
# #                         entry11.destroy()
# #                         entry12.destroy()
# #                         entry13.destroy()
# #                         button11.destroy()
# #                         verifycac.destroy()
# #
# #                         llll = customtkinter.CTkLabel(master=frame, text="Reset Password", font=('Century Gothic', 20))
# #                         llll.place(x=50, y=45)
# #
# #                         entry111 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Enter New Password')
# #                         entry111.place(x=50, y=110)
# #
# #                         entry112 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Confirm New Password',show="*")
# #                         entry112.place(x=50, y=165)
# #
# #                         button111 = customtkinter.CTkButton(master=frame, width=220, text="Reset Password", command=Reset_password,
# #                                                            corner_radius=10, font=('Bold', 20))
# #
# #                         button111.place(x=50, y=270)
# #
# #                     else:
# #                         messagebox.showinfo('Alert',"Incorrect OTP")
# #
# #
# #              else:
# #                  messagebox.showinfo("Alert","Verify All")
# #
# #
# #
# #
# #          user_name_for_password_reset = entry1.get()
# #          if user_name_for_password_reset == "":
# #              messagebox.showinfo("Alert","Please Enter The Username")
# #
# #
# #          elif user_name_for_password_reset in admin_credential:
# #
# #              # messagebox.showinfo("Info","Verify Your Account With OTP")
# #
# #              print(user_name_for_password_reset)
# #              l2.destroy()
# #              entry2.destroy()
# #              entry1.destroy()
# #              l3.destroy()
# #              button1.destroy()
# #
# #
# #
# #
# #
# #
# #              # cccc.text_message()
# #              # otptm=cccc.vvv_Textmessager
# #
# #
# #
# #
# #
# #
# #              lll = customtkinter.CTkLabel(master=frame, text="Verification", font=('Century Gothic', 20))
# #              lll.place(x=50, y=45)
# #
# #              entry11 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Email')
# #              entry11.place(x=50, y=110)
# #
# #
# #              entry12 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Whatsapp')
# #              entry12.place(x=50, y=165)
# #
# #              lowercase = [i for i in string.ascii_lowercase]
# #              uppercase = [i for i in string.ascii_uppercase]
# #              lowercase.extend(uppercase)
# #              cacheee = ""
# #              for i in range(6):
# #                  cccccc = random.choice(lowercase)
# #                  cacheee += cccccc
# #
# #
# #              verifycac=customtkinter.CTkLabel(master=frame,font=('Matura MT Script Capitals', 20),text=f"{cacheee}")
# #              verifycac.place(x=170,y=215)
# #
# #              entry13 = customtkinter.CTkEntry(master=frame, width=100, placeholder_text='Text')
# #              entry13.place(x=50, y=215)
# #
# #
# #
# #              button11 = customtkinter.CTkButton(master=frame, width=220, text="Verify", command=verification,
# #                                                corner_radius=10, font=('Bold', 20))
# #              button11.place(x=50, y=270)
# #
# #              # mail(admin_credential[user_name_for_password_reset]['email'])
# #
# #              cccc = Info(admin_credential[user_name_for_password_reset]['cellular'])
# #
# #              # cccc.whatsapp()
# #              otpwm = cccc.vvv_whatsapp
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #          else:
# #              messagebox.showinfo("Alert", "Enter the Proper Username")
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #     def button_function():
# #         global vvvvv
# #         username=entry1.get()
# #         password=entry2.get()
# #         global numbersss
# #         if username != "" and password != "":
# #             if username in admin_credential :
# #                 g=admin_credential[username]["password"]
# #                 if g == password:
# #                     app.destroy()
# #                     # tkscreen()
# #                 else:
# #                     vvvvv+=1
# #                     messagebox.showinfo("Alert","Incorrect Password")
# #                     if vvvvv > 3:
# #                         # messagebox.showinfo('Alert',"Please Reset Your Password")
# #                         # threading.Thread(target=forgot())
# #                         button1.destroy()
# #                         buttonn1 = customtkinter.CTkButton(master=frame, width=220, text="Login",
# #                                                           command=threading.Thread(target=forgot).start(), corner_radius=10, font=('Bold', 20))
# #                         buttonn1.place(x=50, y=240)
# #                         buttonn1.destroy()
# #
# #
# #
# #
# #             else:
# #
# #                 messagebox.showinfo("Alert", "Incorrect Credential")
# #         else:
# #             messagebox.showinfo("Alert ","Please Provide Your Credential")
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #     img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
# #     l1 = customtkinter.CTkLabel(master=app, image=img1)
# #
# #     l1.pack()
# #
# #
# #     frame = customtkinter.CTkFrame(master=l1, width=690, height=360, corner_radius=15,fg_color=("white"))
# #     frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# #
# #
# #
# #
# #     image = Image.open("login.png")
# #     resise_image = image.resize((380, 380))
# #     img = ImageTk.PhotoImage(resise_image)
# #
# #     image_label = customtkinter.CTkLabel(master=frame,image=img,text="")
# #     image_label.place(x=340, y=25)
# #
# #     l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
# #     l2.place(x=50, y=45)
# #
# #     entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
# #     entry1.place(x=50, y=110)
# #
# #
# #
# #     entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
# #     entry2.place(x=50, y=165)
# #
# #     l3 = customtkinter.CTkButton(master=frame, text="Forget password", font=('Century Gothic', 10),corner_radius=10,width=100,command=threading.Thread(target=forgot).start,fg_color=( "white"),text_color='Black')
# #     l3.place(x=170, y=205)
# #
# #     # Create custom button
# #     button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=10,font=('Bold', 20))
# #     button1.place(x=50, y=240)
# #
# #
# #
# #     app.mainloop()
# #
# # loginpage()
# #
# #
# ##########################################################33
# ############################################################
#
# import time
# from tkinter import *
# from PIL import ImageTk, Image
# import winsound
# from tkinter import messagebox
# from ONE_Finding_donners_screen import Finding_blood_tkscreen
# from TWO_blood_donated_doners_screen import updating_the_date_of_blood_given_donners_tkscreen
# from THREE_donners_registration_portal_screen import donners_registration_tkscreen
# from FOUR_status_update_screen import status_update_tkscreen
# import customtkinter
# import tkinter
#
# class tkscreen():
#     def __init__(self):
#         def find_doner():
#             self.screen.destroy()
#             Finding_blood_tkscreen()
#             tkscreen()
#
#         def Update_date():
#             self.screen.destroy()
#             updating_the_date_of_blood_given_donners_tkscreen()
#             tkscreen()
#         def Status_update():
#             self.screen.destroy()
#             status_update_tkscreen()
#             tkscreen()
#         def registration():
#             self.screen.destroy()
#             donners_registration_tkscreen()
#             tkscreen()
#
#         # self.screen = customtkinter.CTk()
#         #
#         # width, height = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
#         # self.screen.geometry('%dx%d+0+0' % (width, height))
#         #
#         #
#         # self.screen.maxsize(1570, 920)
#         # self.screen.minsize(1270, 720)
#         # self.screen.geometry("1280x720")
#         self.screen.title(string="Menu")
#         self.screen.config(background="white")
#         # self.screen.attributes('fullscreen', True)
#         img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
#         l1 = customtkinter.CTkLabel(master=self.screen, image=img1)
#         l1.pack()
#
#
#         # creating custom frame
#         frame = customtkinter.CTkFrame(master=l1, width=680, height=380, corner_radius=15,fg_color=("white"))
#         # frame.place(x=40, y=160)
#         frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
#
#         image = Image.open("v1.png")
#         resise_image = image.resize((380, 380))
#         img = ImageTk.PhotoImage(resise_image)
#
#         image_label = customtkinter.CTkLabel(master=frame, image=img, text="")
#         image_label.place(x=340, y=30)
#
#         ll2 = customtkinter.CTkLabel(master=frame, text="Menu", font=('Century Gothic', 20))
#         ll2.place(x=50, y=35)
#         #
#
#         #
#
#         self.find_doners = customtkinter.CTkButton(master=frame, width=220, text="Contact Donors",
#                                                                      command=find_doner, corner_radius=10,
#                                                                      font=('Bold', 20))
#         self.find_doners.place(x=70, y=110)
#
#
#
#         self.status_update = customtkinter.CTkButton(master=frame, width=220, text="Status Update",
#                                                                      command=Status_update, corner_radius=10,
#                                                                      font=('Bold', 20))
#         self.status_update.place(x=70, y=160)
#
#
#         self.update_date_of_blood_donation = customtkinter.CTkButton(master=frame, width=220, text="Update Date",
#                                                             command=Update_date, corner_radius=10, font=('Bold', 20))
#         self.update_date_of_blood_donation.place(x=70, y=210)
#
#         self.donners_registration = customtkinter.CTkButton(master=frame, width=220, text="Register", command=registration, corner_radius=10,font=('Bold', 20))
#         self.donners_registration.place(x=70, y=260)
# #
# #
# #
#
#
#
#         self.screen.mainloop()
# # tkscreen()
# #####################################################################################################################################33
# # #importing required modules
# # import tkinter
# # import customtkinter
# # from PIL import ImageTk, Image
# # from admin import admin_credential
# #
# # numbersss = 1
# # def loginpage():
# #     customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# #     customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
# #
# #     app = customtkinter.CTk()
# #
# #     width, height = app.winfo_screenwidth(), app.winfo_screenheight()
# #     app.geometry('%dx%d+0+0' % (width, height))
# #
# #     app.minsize(1280,720)
# #     app.maxsize(1580,920)
# #     app.title('Login Page OF BLoodIndiaConnect')
# #
# #     def button_function():
# #         username=entry1.get()
# #         password=entry2.get()
# #         global numbersss
# #         if username != "" and password != "":
# #             if username in admin_credential :
# #                 g=admin_credential[username]
# #                 if g == password:
# #                     app.destroy()
# #                     tkscreen()
# #                 else:
# #
# #                     messagebox.showinfo("Alert","Incorrect Password")
# #
# #             else:
# #
# #                 messagebox.showinfo("Alert", "Incorrect Credential")
# #         else:
# #             messagebox.showinfo("Alert ","Please Provide Your Credential")
# #         # if adminusername in ap:
# #         #     if ap['adminusername'] == adminpassword:
# #         #
# #         #
# #         #           # destroy current window and creating new one
# #         # # w = customtkinter.CTk()
# #         # # w.geometry("1280x720")
# #         # # w.title('Welcome')
# #         # # l1 = customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
# #         # # l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# #         # # w.mainloop()
# #         #
# #
# #     img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
# #     l1 = customtkinter.CTkLabel(master=app, image=img1)
# #
# #     l1.pack()
# #
# #     # creating custom frame
# #     # frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
# #     # frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# #     #
# #     # l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
# #     # l2.place(x=50, y=45)
# #
# #
# #     frame = customtkinter.CTkFrame(master=l1, width=690, height=360, corner_radius=15,fg_color=("white"))
# #     frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# #
# #
# #     # imggg =PhotoImage(file="C:\\Users\\venkatesan\\Desktop\\im\\login.png")
# #     # Label(app,image=imggg,bg='white').place(x=800,y=280)
# #     #
# #     # image = Image.open("2.jpg")
# #     # resise_image = self.image.resize((270, 400))
# #     # self.img = ImageTk.PhotoImage(self.resise_image)
# #
# #     image = Image.open("login.png")
# #     resise_image = image.resize((380, 380))
# #     img = ImageTk.PhotoImage(resise_image)
# #
# #     image_label = customtkinter.CTkLabel(master=frame,image=img,text="")
# #     image_label.place(x=340, y=25)
# #
# #     l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
# #     l2.place(x=50, y=45)
# #
# #     entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
# #     entry1.place(x=50, y=110)
# #
# #
# #     entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
# #     entry2.place(x=50, y=165)
# #
# #     l3 = customtkinter.CTkLabel(master=frame, text="Forget password", font=('Century Gothic', 12))
# #     l3.place(x=155, y=195)
# #
# #     # Create custom button
# #     button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=10,font=('Bold', 20))
# #     button1.place(x=50, y=240)
# #
# #     # img2 = customtkinter.CTkImage(
# #     #     Image.open("C:\\Users\\venkatesan\\Desktop\\im\\Google__G__Logo.svg.webp").resize((20, 20), Image.ANTIALIAS))
# #     # img3 = customtkinter.CTkImage(
# #     #     Image.open("C:\\Users\\venkatesan\\Desktop\\im\\124010.png").resize((20, 20), Image.ANTIALIAS))
# #     # button2 = customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left",
# #     #                                   fg_color='white', text_color='black', hover_color='#AFAFAF')
# #     # button2.place(x=50, y=290)
# #     #
# #     # button3 = customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left",
# #     #                                   fg_color='white', text_color='black', hover_color='#AFAFAF')
# #     # button3.place(x=170, y=290)
# #
# #     # You can easily integrate authentication system
# #
# #     app.mainloop()
#
# ##################################################################################################################################33
#
# #############################################################################################################################
# import time
# #importing required modules
# import tkinter
# import customtkinter
# from PIL import ImageTk, Image
# from admin import admin_credential
# import tkinter
# from tkinter import messagebox
# from otp_email import mail,vvv
# from whatsapp_cellular_otp import Info
# import threading
# import string
# import random
#
# numbersss = 1
# vvvvv=0
#
#
#
#
# def loginpage():
#     customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
#     customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
#
#     app = customtkinter.CTk()
#
#     width, height = app.winfo_screenwidth(), app.winfo_screenheight()
#     app.geometry('%dx%d+0+0' % (width, height))
#
#     app.minsize(1280,720)
#     app.maxsize(1580,920)
#     app.title('Login')
#
#
#
#
#     def  forgot():
#
#
#
#
#          def verification():
#              def Reset_password():
#
#                  def  againlogin():
#
#                      def afterreset():
#
#                          username = entry1.get()
#                          password = entry2.get()
#                          global numbersss
#                          if username != "" and password != "":
#                              if username in admin_credential:
#                                  g = admin_credential[username]["password"]
#                                  if g == password:
#                                      app.destroy()
#                                      tkscreen()
#                                  else:
#
#                                      messagebox.showinfo("Alert", "Incorrect Password")
#
#
#                              else:
#
#                                  messagebox.showinfo("Alert", "Incorrect Credential")
#                          else:
#                              messagebox.showinfo("Alert ", "Please Provide Your Credential")
#
#                      l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account",
#                                                  font=('Century Gothic', 20))
#                      l2.place(x=50, y=45)
#
#                      entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
#                      entry1.place(x=50, y=110)
#
#                      entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
#                      entry2.place(x=50, y=165)
#
#                      againlogin.destroy()
#
#                      button_for_login=customtkinter.CTkButton(master=frame,text="Login",command=afterreset,corner_radius=10,font=('Bold', 20),width=220)
#                      button_for_login.place(x=50,y=270)
#
#
#                  new_password = entry111.get()
#                  confirm_password = entry112.get()
#
#                  if new_password == "" or confirm_password == "":
#                      messagebox.showinfo('Alert',"Provide New Password")
#                  elif new_password == confirm_password:
#
#                      image_label.destroy()
#
#                      image1 = Image.open("C:\\Users\\venkatesan\\Desktop\\im\\ver.png")
#                      resise_image1 = image1.resize((380, 380))
#                      img1 = ImageTk.PhotoImage(resise_image1)
#
#                      image_label1= customtkinter.CTkLabel(master=frame, image=img1, text="")
#                      image_label1.place(x=340, y=25)
#
#                      admin_credential[user_name_for_password_reset]["password"]= new_password
#                      print(admin_credential)
#
#                      messagebox.showinfo('Info',f"Password Updated Successfully")
#
#                      button111.destroy()
#
#                      againlogin = customtkinter.CTkButton(master=frame,text="Login",command=againlogin,corner_radius=10,font=('Bold', 20))
#                      againlogin.place(x=50 , y= 270)
#
#
#                  else:
#                      messagebox.showinfo('Alert',"Password Doesnot Match")
#
#
#              email = entry11.get()
#              whatsappp = entry12.get()
#              celluar  = entry13.get()
#              # print(type(email),type(vvv))
#              print(cacheee)
#              if email != "" and whatsappp != "" and celluar != "":
#                     if int(email) == vvv  and int(whatsappp) == otpwm:
#                     # if int(email) == vvv and int(whatsappp) == otpwm:
#                         if celluar == cacheee:
#                             lll.destroy()
#                             entry11.destroy()
#                             entry12.destroy()
#                             entry13.destroy()
#                             button11.destroy()
#                             verifycac.destroy()
#
#                             llll = customtkinter.CTkLabel(master=frame, text="Reset Password", font=('Century Gothic', 20))
#                             llll.place(x=50, y=45)
#
#                             entry111 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Enter New Password')
#                             entry111.place(x=50, y=110)
#
#                             entry112 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Confirm New Password',show="*")
#                             entry112.place(x=50, y=165)
#
#                             button111 = customtkinter.CTkButton(master=frame, width=220, text="Reset Password", command=Reset_password,
#                                                                corner_radius=10, font=('Bold', 20))
#
#                             button111.place(x=50, y=270)
#
#                         else:
#                             messagebox.showinfo("Alert","Incorrect Text")
#
#                     else:
#                         messagebox.showinfo('Alert',"Incorrect OTP")
#
#
#              else:
#                  messagebox.showinfo("Alert","Verify All")
#
#
#
#
#          user_name_for_password_reset = entry1.get()
#          if user_name_for_password_reset == "":
#              messagebox.showinfo("Alert","Please Enter The Username")
#
#
#          elif user_name_for_password_reset in admin_credential:
#
#              # messagebox.showinfo("Info","Verify Your Account With OTP")
#
#              print(user_name_for_password_reset)
#              l2.destroy()
#              entry2.destroy()
#              entry1.destroy()
#              l3.destroy()
#              button1.destroy()
#
#
#
#
#
#              # cccc.text_message()
#              # otptm=cccc.vvv_Textmessager
#
#
#
#
#
#
#              lll = customtkinter.CTkLabel(master=frame, text="Verification", font=('Century Gothic', 20))
#              lll.place(x=50, y=45)
#
#              entry11 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Email')
#              entry11.place(x=50, y=110)
#
#
#              entry12 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Whatsapp')
#              entry12.place(x=50, y=165)
#
#
#
#              lowercase = [i for i in string.ascii_lowercase]
#              uppercase = [i for i in string.ascii_uppercase]
#              lowercase.extend(uppercase)
#              cacheee = ""
#              for i in range(6):
#                  cccccc = random.choice(lowercase)
#                  cacheee += cccccc
#
#              verifycac = customtkinter.CTkLabel(master=frame, font=('Matura MT Script Capitals', 20), text=f"{cacheee}")
#              verifycac.place(x=170, y=215)
#
#
#
#              entry13 = customtkinter.CTkEntry(master=frame, width=110, placeholder_text='Text')
#              entry13.place(x=50, y=215)
#
#              button11 = customtkinter.CTkButton(master=frame, width=220, text="Verify", command=verification,
#                                                corner_radius=10, font=('Bold', 20))
#              button11.place(x=50, y=270)
#
#              messagebox.showinfo("Info", "Verify Your Account With OTP")
#
#              mail(admin_credential[user_name_for_password_reset]['email'])
#
#              cccc = Info(admin_credential[user_name_for_password_reset]['cellular'])
#
#              cccc.whatsapp()
#              otpwm = cccc.vvv_whatsapp
#
#
#
#
#
#
#
#
#          else:
#              messagebox.showinfo("Alert", "Enter the Proper Username")
#
#
#
#
#
#
#
#
#
#
#
#     def button_function():
#         global vvvvv
#         username=entry1.get()
#         password=entry2.get()
#         global numbersss
#         if username != "" and password != "":
#             if username in admin_credential :
#                 g=admin_credential[username]["password"]
#                 if g == password:
#                     app.destroy()
#                     tkscreen()
#                 else:
#                     vvvvv+=1
#                     messagebox.showinfo("Alert","Incorrect Password")
#                     if vvvvv > 3:
#                       # threading.Thread(target=forgot())
#                       button1.destroy()
#                       buttonn1 = customtkinter.CTkButton(master=frame, width=220, text="Login",
#                                                          command=threading.Thread(target=forgot).start(),
#                                                          corner_radius=10, font=('Bold', 20))
#                       buttonn1.place(x=50, y=240)
#                       buttonn1.destroy()
#
#
#             else:
#
#                 messagebox.showinfo("Alert", "Incorrect Credential")
#         else:
#             messagebox.showinfo("Alert ","Please Provide Your Credential")
#
#
#
#
#
#
#
#
#
#     img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
#     l1 = customtkinter.CTkLabel(master=app, image=img1)
#
#     l1.pack()
#
#
#     frame = customtkinter.CTkFrame(master=l1, width=690, height=360, corner_radius=15,fg_color=("white"))
#     frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
#
#
#
#     image = Image.open("login.png")
#     resise_image = image.resize((380, 380))
#     img = ImageTk.PhotoImage(resise_image)
#
#     image_label = customtkinter.CTkLabel(master=frame,image=img,text="")
#     image_label.place(x=340, y=25)
#
#     l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
#     l2.place(x=50, y=45)
#
#     entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
#     entry1.place(x=50, y=110)
#
#
#
#     entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
#     entry2.place(x=50, y=165)
#
#     l3 = customtkinter.CTkButton(master=frame, text="Forget password", font=('Century Gothic', 10),corner_radius=10,width=100,command=threading.Thread(target=forgot).start,fg_color=( "white"),text_color='Black')
#     l3.place(x=170, y=205)
#
#     # Create custom button
#     button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=10,font=('Bold', 20))
#     button1.place(x=50, y=240)
#
#
#
#     app.mainloop()
#
#
#
#
# ######################################################################################################################################3
#
#
#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import time

w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    # loginpage()
    # tkscreen()
    pass

Frame(w, width=427, height=1250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='BloodIndiaConnect', fg='white', bg='#272727') #decorate it
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

# la=Label(text="Connecting Donors with Hospital",fg='white', bg ='#272727')
# la.configure(font=("Game of Squid",10,"bold"))
# la.place(x=80,y=100)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\c2.png"))
image_b=ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\c1.png"))


# time.sleep(5)

for i in range(1): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
new_win()
w.mainloop()
#
#
