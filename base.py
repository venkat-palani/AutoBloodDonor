import pyrebase
firebaseConfig = {
  'apiKey': "AIzaSyApIeFcUTeVNNKbnbJb_HVW6IRP_NhwBSs",
  'authDomain': "indiaconnect-e7e2f.firebaseapp.com",
  'projectId': "indiaconnect-e7e2f",
  'storageBucket': "indiaconnect-e7e2f.appspot.com",
  'messagingSenderId': "236695238867",
  'appId': "1:236695238867:web:0d95b87b5da2745eb27c26",
  'databaseURL':"https://indiaconnect-e7e2f-default-rtdb.firebaseio.com",
  'measurementId': "G-MEJS2WWRFV"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login(emaill,password):
    try:
        hhh=auth.sign_in_with_email_and_password(emaill,password)

        # print("Successfully Logged in...")
        return 0
    except:
        # print("Invalid Email or Password")
        return 1

def forgot_password(emailid):
    try:
        auth.send_password_reset_email(emailid)
        return 0
    except:
        return 1
#
# def signup():
#     print("Sign Up....")
#     emaill = input("Enter Email:")
#     password = input("Enter password")
#
#     try:
#         user = auth.create_user_with_email_and_password(emaill,password)
#     except:
#         print("Email already exists")
#     return
# ans = input("Are you are new user")
#
# if ans == "n":
#     login()
# elif ans == "y":
#     signup()