# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox
# from ONE_donersdatabase import finallistofsuitabledoners
# from FOUR_status_update_info import Info
#
# class status_update_tkscreen():
#     def __init__(self):
#         def commandd():
#                self.pat_name = self.patient_name.get()
#                self.pat_blood_group = self.blood_group.get()
#                self.city = self.cities.get()
#                self.address = self.address_text.get('1.0',END)
#                a=str(self.address).split()
#                if self.pat_name != "" and self.pat_blood_group != "Select The Blood Group" and self.city != "Select The City" and a != []:
#                     self.button["state"] = DISABLED
#                     gg=finallistofsuitabledoners(self.pat_blood_group,self.city)
#                     print(gg.donersfinallist)
#
#                     for i in gg.donersfinallist:
#                            dddd=Info(self.pat_name,i[3],self.address)
#                            dddd.whatsapp()
#                            # dddd.text_message()
#                     print(self.city,self.pat_name,self.pat_blood_group,self.address)
#                     try:
#                         answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
#                         Label(text=answer, font=('Arial 20 bold')).pack()
#                     except:
#                         pass
#                else:
#                    try:
#                        answer = messagebox.showinfo("INFO", "Please Enter All Fields")
#                        Label(text=answer, font=('Arial 20 bold')).pack()
#                    except:
#                        pass
#
#
#         self.screen_Four = Tk()
#         self.screen_Four.maxsize(950, 950)
#         self.screen_Four.minsize(950, 950)
#         self.screen_Four.title(string="Auto Contact Blood Don0rs")
#
#         self.info = Label(text="STATUS UPDATE")
#         self.info.grid(column=0, row=0)
#         self.info.config(font=("Arial", 22, "bold"))
#         self.info.config(pady=20, padx=350)
#
#         self.donners_name_label = Label(text="Enter the Patient's Name Below :")
#         self.donners_name_label.grid(column=0, row=1)
#         self.donners_name_label.config(font=("Arial", 15, "bold"))
#         self.donners_name_label.config(pady=20)
#
#         self.patient_name = Entry(width=50)
#         self.patient_name.grid(column=0, row=2)
#         self.patient_name.focus()
#
#         self.donners_blood_group_label = Label(text="Select the Patient's Blood Group:")
#         self.donners_blood_group_label.grid(column=0, row=3)
#         self.donners_blood_group_label.config(pady=20)
#         self.donners_blood_group_label.config(font=("Arial", 15, "bold"))
#
#         self.blood_group = StringVar(self.screen_Four)
#         self.blood_group.set("Select The Blood Group")
#         self.list_of_blood_group = OptionMenu(self.screen_Four, self.blood_group, "a positive", "a negative", "b positive",
#                                               "b negative"
#                                               , "ab positive", "ab negative", "o positive", "o negative")
#         self.list_of_blood_group.grid(column=0, row=4)
#         self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)
#
#
#         self.donners_locatiom = Label(text="Select the Location\City:")
#         self.donners_locatiom.grid(column=0, row=5)
#         self.donners_locatiom.config(pady=20)
#         self.donners_locatiom.config(font=("Arial", 15, "bold"))
#
#         self.cities = StringVar(self.screen_Four)
#         self.cities.set("Select The City")
#         self.list_of_location = OptionMenu(self.screen_Four, self.cities, "coimbatore", "chennai", "hosur", "madurai",
#                                            "karaikudi", "karur",
#                                            "trichy", "namkal")
#         self.list_of_location.grid(column=0, row=6)
#         self.list_of_location.config(height=2, highlightbackground="red", highlightcolor="blue", highlightthickness=10)
#
#         self.addressd = Label(text=f"Enter the Address")
#         self.addressd.grid(column=0, row=9)
#         self.addressd.config(pady=20)
#         self.addressd.config(font=("Arial", 15, "bold"))
#         #
#         self.address_text = Text(width=40, height=5)
#         self.address_text.grid(column=0, row=10)
#
#         # self.button = Button(self.screen,command=threading.Thread(target=commandd).start)
#
#         self.button = Button(command=commandd)
#         self.button.config(text="Inform To Donors")
#         self.button.place(x=330, y=689)
#         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#
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
#         self.screen_Four.mainloop()

#############################################################################################################################
# import time
# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import messagebox
# from ONE_donersdatabase import finallistofsuitabledoners
# from FOUR_status_update_info import Info
# from ONE_patientdatabade import Patient_datas
# import  threading
#
# class status_update_tkscreen():
#     def __init__(self):
#         def commandd():
#                self.patientid = self.patient_id_entry.get()
#                if self.patientid != "Enter If Known" and self.patientid != "" :
#                    self.button["state"] = DISABLED
#                    self.p=Patient_datas(int(self.patientid))
#                    self.patient_name.insert(0,f"{self.p.patientname}")
#                    self.blood_group.set(f"{self.p.patientbloodgroup}")
#                    self.cities.set(f"{self.p.city}")
#                    self.address_text.insert(END,f"{self.p.location}")
#
#                    self.pat_name = self.p.patientname
#                    self.pat_blood_group = self.p.patientbloodgroup
#                    self.city = self.p.city
#                    self.address = self.p.location
#                    gg = finallistofsuitabledoners(self.pat_blood_group, self.city)
#                    print(gg.donersfinallist)
#
#                    for i in gg.donersfinallist:
#                        dddd = Info(self.pat_name, i[3], self.address)
#                        dddd.whatsapp()
#                        # dddd.text_message()
#                    print(self.city, self.pat_name, self.pat_blood_group, self.address)
#
#                    try:
#                        answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
#                        Label(text=answer, font=('Arial 20 bold')).pack()
#                    except:
#                        pass
#
#
#
#
#                else:
#
#                    self.pat_name = self.patient_name.get()
#                    self.pat_blood_group = self.blood_group.get()
#                    self.city = self.cities.get()
#                    self.address = self.address_text.get('1.0',END)
#                    a=str(self.address).split()
#
#
#                    if self.pat_name != "" and self.pat_blood_group != "Select The Blood Group" and self.city != "Select The City" and a != []:
#                         self.button["state"] = DISABLED
#                         gg=finallistofsuitabledoners(self.pat_blood_group,self.city)
#                         print(gg.donersfinallist)
#
#                         for i in gg.donersfinallist:
#                                dddd=Info(self.pat_name,i[3],self.address)
#                                dddd.whatsapp()
#                                # dddd.text_message()
#                         print(self.city,self.pat_name,self.pat_blood_group,self.address)
#                         try:
#                             answer = messagebox.showinfo("INFO", "Successfully Informed Donors")
#                             Label(text=answer, font=('Arial 20 bold')).pack()
#                         except:
#                             pass
#                    else:
#                        try:
#                            answer = messagebox.showinfo("INFO", "Please Enter All Fields")
#                            Label(text=answer, font=('Arial 20 bold')).pack()
#                        except:
#                            pass
#
#
#         self.screen_Four = Tk()
#         self.screen_Four.maxsize(950, 950)
#         self.screen_Four.minsize(950, 950)
#         self.screen_Four.title(string="Auto Contact Blood Don0rs")
#
#         self.info = Label(text="STATUS UPDATE")
#         self.info.grid(column=0, row=0)
#         self.info.config(font=("Arial", 22, "bold"))
#         self.info.config(pady=20, padx=350)
#
#         self.patient_id = Label(text="Patient id")
#         self.patient_id.grid(column=0, row=1)
#         self.patient_id.config(font=("Arial", 15, "bold"))
#         self.patient_id.config(pady=10)
#
#
#         def click(*args):
#             self.patient_id_entry.delete(0, 'end')
#
#
#         self.patient_id_entry = Entry(self.screen_Four, width=50)
#
#         # Add text in Entry box
#         self.patient_id_entry.insert(0, 'Enter If Known')
#         self.patient_id_entry.grid(column=0, row=2)
#
#         # Use bind method
#         self.patient_id_entry.bind("<Button-1>", click)
#
#         self.donners_name_label = Label(text="Or")
#         self.donners_name_label.grid(column=0, row=3)
#         self.donners_name_label.config(font=("Arial", 15, "bold"))
#         self.donners_name_label.config(pady=10)
#
#         self.donners_name_label = Label(text="Enter the Patient's Name Below :")
#         self.donners_name_label.grid(column=0, row=4)
#         self.donners_name_label.config(font=("Arial", 15, "bold"))
#         self.donners_name_label.config(pady=10)
#
#         self.patient_name = Entry(width=50)
#         self.patient_name.grid(column=0, row=5)
#         self.patient_name.focus()
#
#         self.donners_blood_group_label = Label(text="Select the Patient's Blood Group:")
#         self.donners_blood_group_label.grid(column=0, row=6)
#         self.donners_blood_group_label.config(pady=20)
#         self.donners_blood_group_label.config(font=("Arial", 15, "bold"))
#
#         self.blood_group = StringVar(self.screen_Four)
#         self.blood_group.set("Select The Blood Group")
#         self.list_of_blood_group = OptionMenu(self.screen_Four, self.blood_group, "a positive", "a negative", "b positive",
#                                               "b negative"
#                                               , "ab positive", "ab negative", "o positive", "o negative")
#         self.list_of_blood_group.grid(column=0, row=7)
#         self.list_of_blood_group.config(height=2, highlightbackground="red", highlightthickness=10)
#
#
#         self.donners_locatiom = Label(text="Select the Location\City:")
#         self.donners_locatiom.grid(column=0, row=8)
#         self.donners_locatiom.config(pady=20)
#         self.donners_locatiom.config(font=("Arial", 15, "bold"))
#
#         self.cities = StringVar(self.screen_Four)
#         self.cities.set("Select The City")
#         self.list_of_location = OptionMenu(self.screen_Four, self.cities, "coimbatore", "chennai", "hosur", "madurai",
#                                            "karaikudi", "karur",
#                                            "trichy", "namkal")
#         self.list_of_location.grid(column=0, row=9)
#         self.list_of_location.config(height=2, highlightbackground="red", highlightcolor="blue", highlightthickness=10)
#
#         self.addressd = Label(text=f"Enter the Address")
#         self.addressd.grid(column=0, row=10)
#         self.addressd.config(pady=20)
#         self.addressd.config(font=("Arial", 15, "bold"))
#         #
#         self.address_text = Text(width=40, height=5)
#         self.address_text.grid(column=0, row=11)
#
#
#         # self.button = Button(self.screen_Four,command=threading.Thread(target=commandd).start)
#         self.button = Button(command=commandd)
#         self.button.config(text="Inform To Donors")
#         self.button.place(x=330, y=689)
#         self.button.config(font=("Arial", 20, "bold"), highlightthickness=0)
#
#
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
#         self.screen_Four.mainloop()


##########################################################################################################################





import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from ONE_donersdatabase import finallistofsuitabledoners
from FOUR_status_update_info import Info
from ONE_patientdatabade import Patient_datas
import customtkinter
import tkinter
import  threading

class status_update_tkscreen():
    def __init__(self):
        def commandd():
               self.patientid = self.patient_id_entry.get()
               if self.patientid != "Enter If Known" and self.patientid != "" :
                   self.button["state"] = DISABLED
                   self.p=Patient_datas(int(self.patientid))
                   self.patient_name.insert(0,f"{self.p.patientname}")
                   self.blood_group.set(f"{self.p.patientbloodgroup}")
                   self.cities.set(f"{self.p.city}")
                   self.address_text.insert(END,f"{self.p.location}")

                   self.pat_name = self.p.patientname
                   self.pat_blood_group = self.p.patientbloodgroup
                   self.city = self.p.city
                   self.address = self.p.location
                   gg = finallistofsuitabledoners(self.pat_blood_group, self.city)
                   print(gg.donersfinallist)

                   for i in gg.donersfinallist:
                       dddd = Info(self.pat_name, i[3], self.address)
                       dddd.whatsapp()
                       # dddd.text_message()
                   print(self.city, self.pat_name, self.pat_blood_group, self.address)

                   try:
                       answer = messagebox.showinfo("INFO", "Successfully Informed To Donors")
                       Label(text=answer, font=('Arial 20 bold')).pack()
                   except:
                       pass




               else:

                   self.pat_name = self.patient_name.get()
                   self.pat_blood_group = self.blood_group.get()
                   self.city = self.cities.get()
                   self.address = self.address_text.get()
                   a=str(self.address).split()


                   if self.pat_name != "" and self.pat_blood_group != "Select The Blood Group" and self.city != "Select The City" and a != []:
                        # self.button["state"] = DISABLED
                        self.button['state'] = DISABLED
                        gg=finallistofsuitabledoners(self.pat_blood_group,self.city)
                        print(gg.donersfinallist)

                        for i in gg.donersfinallist:
                               dddd=Info(self.pat_name,i[3],self.address)
                               dddd.whatsapp()
                               # dddd.text_message()
                        print(self.city,self.pat_name,self.pat_blood_group,self.address)
                        try:
                            answer = messagebox.showinfo("INFO", "Successfully Informed To Donors")
                            Label(text=answer, font=('Arial 20 bold')).pack()
                        except:
                            pass
                   else:
                       try:
                           answer = messagebox.showinfo("INFO", "Please Enter All Fields")
                           Label(text=answer, font=('Arial 20 bold')).pack()
                       except:
                           pass


        self.screen_Four = customtkinter.CTk()

        width, height = self.screen_Four.winfo_screenwidth(), self.screen_Four.winfo_screenheight()
        self.screen_Four.geometry('%dx%d+0+0' % (width, height))

        # self.screen_Four.maxsize(1270, 720)
        # self.screen_Four.minsize(1270, 720)

        self.screen_Four.title(string="Status Update")

        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
        l1 = customtkinter.CTkLabel(master=self.screen_Four, image=img1)
        l1.pack()

        frame = customtkinter.CTkFrame(master=l1, width=500, height=470, corner_radius=15)
        # frame.place(x=40, y=160)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.ll2 = customtkinter.CTkLabel(master=frame, text="Status Update", font=('Century Gothic', 20))
        self.ll2.place(x=50, y=35)

        self.patient_id = customtkinter.CTkLabel(master=frame, text="Patient id", font=('Century Gothic', 15))
        self.patient_id.place(x=50, y=90)

        def click(*args):
            self.patient_id_entry.delete(0, 'end')

        self.patient_id_entry = customtkinter.CTkEntry(master=frame, width=200)
        self.patient_id_entry.insert(0, 'Enter If Known')
        self.patient_id_entry.place(x=250, y=90)
        self.patient_id_entry.bind("<Button-1>", click)



        self.donners_name_label = customtkinter.CTkLabel(master=frame,text="Enter the Patient's Name",font=('Century Gothic',15))
        self.donners_name_label.place(x=50,y=140)


        self.patient_name = customtkinter.CTkEntry(master=frame,width=200)
        self.patient_name.place(x=250,y=140)
        self.patient_name.focus()

        self.donners_blood_group_label = customtkinter.CTkLabel(master=frame,text="Patient's Blood Group",font=('Century Gothic',15))
        self.donners_blood_group_label.place(x=50,y=190)


        # self.blood_group = StringVar(self.screen_Four)
        # self.blood_group.set("Select The Blood Group")
        self.blood_group = customtkinter.CTkOptionMenu(master=frame,
                                                       values=["a positive", "a negative", "b positive",
                                              "b negative"
                                              , "ab positive", "ab negative", "o positive", "o negative"],width=200)
        self.blood_group.place(x=250,y=190)
        self.blood_group.set('Blood Group')



        self.donners_locatiom = customtkinter.CTkLabel(master=frame,text="Location\City",font=('Century Gothic',15))
        self.donners_locatiom.place(x=50,y=240)


        # self.cities = StringVar(self.screen_Four)
        # self.cities.set("Select The City")
        self.cities = customtkinter.CTkOptionMenu(master=frame,
                                                  values=["coimbatore", "chennai", "hosur", "madurai",
                                           "karaikudi", "karur",
                                           "trichy", "namkal"],width=200)
        self.cities.place(x=250,y=240)


        self.addressd = customtkinter.CTkLabel(master=frame,text="Hospital Name",font=('Century Gothic',15))
        self.addressd.place(x=50,y=290)

        #
        self.address_text = customtkinter.CTkEntry(master=frame, width=200)
        self.address_text.place(x=250,y=290)





        self.button = customtkinter.CTkButton(master=frame, width=220, text="Inform", command=commandd,
                                          corner_radius=10,font=('Bold', 20))
        self.button.place(x=150, y=400)



        self.screen_Four.mainloop()




