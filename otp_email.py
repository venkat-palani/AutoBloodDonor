from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
import random




v=0
bb=1

subject=[i for i in range(300000,1000000)]
vvv=random.choice(subject)
# mail_id=['venkatesanpalani21@gmail.com']
def mail(mail_id):
     global vvv
     global bb
     try:
        for i in range(bb):
            # for i in mail_id:
                global v
                strFrom = 'BloodIndiaConnect@gmail.com'
                password="mbehzkvlgisqotqw"
                # Create the root message and fill in the from, to, and subject headers
                msgRoot = MIMEMultipart('alternative')

                print(vvv)
                msgRoot['Subject'] = "One Time Password (OTP) for Reset Password on BloodIndiaConnect "
                # print(msgRoot['Subject'])

                msgRoot.preamble = 'This is a multi-part message in MIME format.'

                # Encapsulate the plain and HTML versions of the message body in an
                # 'alternative' part, so message agents can decide which they want to display.
                msgAlternative = MIMEMultipart('alternative')
                msgRoot.attach(msgAlternative)

                # msgText1 = MIMEText('Wwlcome Buddy')
                # msgAlternative.attach(msgText)

                # We reference the image in the IMG SRC attribute by the ID we give it below
                msgText2 = MIMEText(f"<h1>Dear Customer</h1> <p> <h3>Your One Time Password(OTP) for Reset of password on BloodIndiaConnect is <br><br> {vvv}</h3></p><p> <footer>Regards :BloodIndiaConnect <br> <a href=></a>{strFrom}</p>","html")

                # msgText3 = MIMEText(f"<h1>&#127761;&#127762;&#127763;&#127764;&#127765;&#127766; </h1> <a href=></a>{i}</p>",
                #     "html")
                # random_message=(msgText1,msgText2,msgText3)
                msgAlternative.attach(msgText2)



                # This example assumes the image is in the current directory
                # fp = open(f"sl/{random.randint(1,23)}.jpg", 'rb')
                # # fp = open(f"sl/1.jpg", 'rb')
                # msgImage = MIMEImage(fp.read())
                # fp.close()
                #
                # # Define the image's ID as referenced above
                # msgImage.add_header('Content-ID', '<image1>')
                # msgRoot.attach(msgImage)

                # Send the email (this example assumes SMTP authentication is required)



                connection=smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=strFrom,password=password)
                connection.sendmail(from_addr=strFrom,to_addrs=mail_id,msg=msgRoot.as_string())
                connection.quit()
                v+=1
                # print(v)
                bb-=1
                print(f"{v}:{bb}")

     except  smtplib.SMTPServerDisconnected:
           import time
           time.sleep(15)
           # mail()

     except smtplib.SMTPDataError:
         print("Sorry Ur Daily Quota Exceeded")


     except:
          # mail()
          pass
# mail("venkatesan2122002@gmail.com")



