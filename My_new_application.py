import os
import time
import webbrowser
import lk_email
"""
#---------------------------lk_email.py---------------------------------
import smtplib
import random as rd

smtobj=smtplib.SMTP('smtp.gmail.com',587)
smtobj.ehlo()
smtobj.starttls()
smtobj.ehlo
smtobj.login('lkapp544@gmail.com','Lakshmikanth2003')
pwd=rd.randrange(100000,999999)
msg=f'Subject:OTP for verification \n\n OTP is '
def otp():
	to=input("Please enter your email address[to verify]:")
	smtobj.sendmail('lkapp544@gmail@gmail.com',to,msg+str(pwd))	
	
smtobj.quit
#---------------------------------------------------------------------------
"""
def clear():
	os.system('cls')

print("Welcome to Lakshmikanth_first_program")
time.sleep(3)
clear()
user=input("Username:")
users=dir(r"C:\\Lakshmikanth_first_program_files\users")
clear()
if user not in users:
	try:
		otp()
		for i in range(100):
			lk=int(input("Please enter OTP:"))
			if lk == pwd:
				break
		dir=user
		parent_dir=r"C:\\Lakshmikanth_first_program_files\users"
		path=os.path.join(parent_dir,dir)
		os.mkdir(path)
		time.sleep(3)
		print("Hello",user,"Your profile has been created sucessfully")

else:
	print("Thank you",user,"for comming back again")
for i in range(5):
	print(".")
	time.sleep(1)
clear()
do=input("what can I search for you?")
time.sleep(1)

webbrowser.open('https://www.google.com/search?b-d&q='+do)
clear()