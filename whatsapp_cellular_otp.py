from twilio.rest import Client
from  account_details import  account_detailss
import random

class Info:
    def __init__(self,number):
        self.accdet = account_detailss()
        self.client = Client(self.accdet.account_sid, self.accdet.account_token)
        self.number= number




    def whatsapp(self):
        self.subject_whatsapp = [i for i in range(300000, 1000000)]
        self.vvv_whatsapp = random.choice(self.subject_whatsapp)
        self.message = self.client.messages \
            .create(to=f'whatsapp:+91{self.number}', from_='whatsapp:+14155238886',
                    body=f"Your One Time Password for Reset of Password on BloodIndiaConnect is {self.vvv_whatsapp}")




    # def text_message(self):
    #     self.subject_Textmessager = [i for i in range(300000, 1000000)]
    #     self.vvv_Textmessager = random.choice(self.subject_Textmessager)
    #     self.message = self.client.messages \
    #         .create(
    #
    #         body=f"Your One Time Password for Reset of Password on BloodIndiaConnect is {self.vvv_Textmessager}",
    #         from_="+12184276439",
    #         to=f"+91 {self.number}"
    #     )

