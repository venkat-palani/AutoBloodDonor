from ONE_Finding_donners_screen import Finding_blood_tkscreen
from TWO_blood_donated_doners_screen import updating_the_date_of_blood_given_donners_tkscreen
from THREE_donners_registration_portal_screen import donners_registration_tkscreen
from FOUR_status_update_screen import status_update_tkscreen
import customtkinter
import tkinter

class tkscreen():
    def __init__(self):
        def find_doner():
            self.screen.destroy()
            Finding_blood_tkscreen()
            tkscreen()

        def Update_date():
            self.screen.destroy()
            updating_the_date_of_blood_given_donners_tkscreen()
            tkscreen()
        def Status_update():
            self.screen.destroy()
            status_update_tkscreen()
            tkscreen()
        def registration():
            self.screen.destroy()
            donners_registration_tkscreen()
            tkscreen()
        self.screen = customtkinter.CTk()

        width, height = self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()
        self.screen.geometry('%dx%d+0+0' % (width, height))


        self.screen.maxsize(1570, 920)
        self.screen.minsize(1270, 720)
        # self.screen.geometry("1280x720")
        self.screen.title(string="Menu")
        self.screen.config(background="white")
        # self.screen.attributes('fullscreen', True)
        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
        l1 = customtkinter.CTkLabel(master=self.screen, image=img1)
        l1.pack()


        # creating custom frame
        frame = customtkinter.CTkFrame(master=l1, width=680, height=380, corner_radius=15,fg_color=("white"))
        # frame.place(x=40, y=160)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


        image = Image.open("v1.png")
        resise_image = image.resize((380, 380))
        img = ImageTk.PhotoImage(resise_image)

        image_label = customtkinter.CTkLabel(master=frame, image=img, text="")
        image_label.place(x=340, y=30)

        # image = Image.open("v1.png")
        # resise_image = image.resize((380, 380))
        # img = ImageTk.PhotoImage(resise_image)
        #
        # image_label = customtkinter.CTkLabel(master=frame, image=img, text="")
        # image_label.place(x=380, y=90)

        ll2 = customtkinter.CTkLabel(master=frame, text="Menu", font=('Century Gothic', 20))
        ll2.place(x=50, y=35)
        #

        #

        self.find_doners = customtkinter.CTkButton(master=frame, width=220, text="Contact Donors",
                                                                     command=find_doner, corner_radius=10,
                                                                     font=('Bold', 20))
        self.find_doners.place(x=70, y=110)



        self.status_update = customtkinter.CTkButton(master=frame, width=220, text="Status Update",
                                                                     command=Status_update, corner_radius=10,
                                                                     font=('Bold', 20))
        self.status_update.place(x=70, y=160)


        self.update_date_of_blood_donation = customtkinter.CTkButton(master=frame, width=220, text="Update Date",
                                                            command=Update_date, corner_radius=10, font=('Bold', 20))
        self.update_date_of_blood_donation.place(x=70, y=210)

        self.donners_registration = customtkinter.CTkButton(master=frame, width=220, text="Register", command=registration, corner_radius=10,font=('Bold', 20))
        self.donners_registration.place(x=70, y=260)
#
#
#



        self.screen.mainloop()
# tkscreen()
#####################################################################################################################################33
# #importing required modules
# import tkinter
# import customtkinter
# from PIL import ImageTk, Image
# from admin import admin_credential
#
# numbersss = 1
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
#     app.title('Login Page OF BLoodIndiaConnect')
#
#     def button_function():
#         username=entry1.get()
#         password=entry2.get()
#         global numbersss
#         if username != "" and password != "":
#             if username in admin_credential :
#                 g=admin_credential[username]
#                 if g == password:
#                     app.destroy()
#                     tkscreen()
#                 else:
#
#                     messagebox.showinfo("Alert","Incorrect Password")
#
#             else:
#
#                 messagebox.showinfo("Alert", "Incorrect Credential")
#         else:
#             messagebox.showinfo("Alert ","Please Provide Your Credential")
#         # if adminusername in ap:
#         #     if ap['adminusername'] == adminpassword:
#         #
#         #
#         #           # destroy current window and creating new one
#         # # w = customtkinter.CTk()
#         # # w.geometry("1280x720")
#         # # w.title('Welcome')
#         # # l1 = customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
#         # # l1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#         # # w.mainloop()
#         #
#
#     img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\venkatesan\\Desktop\\im\\pattern.png"))
#     l1 = customtkinter.CTkLabel(master=app, image=img1)
#
#     l1.pack()
#
#     # creating custom frame
#     # frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
#     # frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#     #
#     # l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
#     # l2.place(x=50, y=45)
#
#
#     frame = customtkinter.CTkFrame(master=l1, width=690, height=360, corner_radius=15,fg_color=("white"))
#     frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
#
#     # imggg =PhotoImage(file="C:\\Users\\venkatesan\\Desktop\\im\\login.png")
#     # Label(app,image=imggg,bg='white').place(x=800,y=280)
#     #
#     # image = Image.open("2.jpg")
#     # resise_image = self.image.resize((270, 400))
#     # self.img = ImageTk.PhotoImage(self.resise_image)
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
#     entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
#     entry2.place(x=50, y=165)
#
#     l3 = customtkinter.CTkLabel(master=frame, text="Forget password", font=('Century Gothic', 12))
#     l3.place(x=155, y=195)
#
#     # Create custom button
#     button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=10,font=('Bold', 20))
#     button1.place(x=50, y=240)
#
#     # img2 = customtkinter.CTkImage(
#     #     Image.open("C:\\Users\\venkatesan\\Desktop\\im\\Google__G__Logo.svg.webp").resize((20, 20), Image.ANTIALIAS))
#     # img3 = customtkinter.CTkImage(
#     #     Image.open("C:\\Users\\venkatesan\\Desktop\\im\\124010.png").resize((20, 20), Image.ANTIALIAS))
#     # button2 = customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left",
#     #                                   fg_color='white', text_color='black', hover_color='#AFAFAF')
#     # button2.place(x=50, y=290)
#     #
#     # button3 = customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left",
#     #                                   fg_color='white', text_color='black', hover_color='#AFAFAF')
#     # button3.place(x=170, y=290)
#
#     # You can easily integrate authentication system
#
#     app.mainloop()

##################################################################################################################################33

#############################################################################################################################normal
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
#
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

##############################################FIREBASE##################################################################3

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
from base import login ,forgot_password

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
        
        # usernameadd=username+"@gmail.com"
        # print(usernameadd)

        if username != "" and password != "":
            ddd = login(username, password)
            if ddd == 0:
                app.destroy()
                tkscreen()

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

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Email')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=10,
                                      font=('Bold', 20))
    button1.place(x=50, y=240)

    l3 = customtkinter.CTkButton(master=frame, text="Forget password", font=('Century Gothic', 10), corner_radius=10,
                                 width=100, command=fogot, fg_color=("white"),
                                 text_color='Black')
    l3.place(x=170, y=205)

    app.mainloop()





######################################################################################################################################3


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
    loginpage()
    # tkscreen()

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

for i in range(5): #5loops
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


