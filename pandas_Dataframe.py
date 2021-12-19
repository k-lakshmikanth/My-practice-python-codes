import pandas as pd
import os

id=[1,2,3,4]
name=["Lakshmikanth","Keerthi","Sai","Eeshan"]
age=[18,10,11,2]

data={"student_id":id,
			"student_name":name,
			"age":age
				}	
for i in range(100):
	x=input("read or append[case sensitive]:")
	if x == "append":
		a=int(input("id:"))
		b=input("name:")
		c=int(input("age:"))
	
		id.append(a)
		name.append(b)
		age.append(c)
		df=pd.DataFrame(data)
		df.to_excel("pandas_dataframe_excel.xlsx",sheet_name="lk")
		print(df)
		break
	elif x == "read":
		f=open('pandas_dataframe_excel.xlsx','r')
		for i in f:
			print(i)
		break
	else:
		print("ERROR incorrect input.")

