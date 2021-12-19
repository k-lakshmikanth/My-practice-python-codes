import os
import time

def cls():
	os.system('cls')

print("Hello world")
time.sleep(3)
cls()
print(time.ctime())
os.chdir(r"C:\Users\Keerthi\Desktop\LK")
f=open('Test.txt','rt')
print(f.read())
f.close()
f=open('Test.txt','a')
f.write("\n"+time.ctime()+"-'Test successful'")
f.close()
