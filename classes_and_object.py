class person :

 def __init__(self,n,g,a):
  self.name=n
  self.gender=g
  self.age=a

 def talk(self):
  print("Hi I am ",self.name)
  
 def vote(self):
  if self.age<18 :
   print("I am not eligible to vote")
  else:
   print("I am eligible to vote") 

obj1=person("sam","Male",22)
obj2=person("Mia","Female",18)
lk=person("Lakshmikanth","Male",18)

obj1.talk()
obj1.vote()
obj2.talk()
obj2.vote()

print(lk.name)