print("Hello")

from mailer import Mailer
mail=Mailer(email='lakshmikanthkasapuram007@gmail.com',password='Lakshmikanth2003')
mail.send(recevier='lakshmikanthkasapuram007@gmail.com',subject='Test',message='This is a test mail')

print('done')