import pandas as pd

pd.read_excel("House.xlsx")

l_area = [120]
l_price = [5000000]
no_bedr = [2]
k_type = ["normal"]
c_price = [10000000]

t_price = l_price + c_price


data = {"Land area(in sq.feet):":l_area,
		"Land cost(in INR):":l_price,
		"No. of bedrooms:":no_bedr,
		"Kitchen type(open or normal):":k_type,
		"Construction cost:":c_price,
		"Total cost to pay:":t_price
		}
		
for i in range(10):
	a=int(input("Land area(in sq.feet):"))
	b=int(input("Land cost(in INR):"))
	c=int(input("No. of bedrooms:"))
	d=input("Kitchen type(open or normal):")
	e=int(input("Construction cost:"))
	
	l_area.append(a)
	l_price.append(b)
	no_bedr.append(c)
	k_type.append(d)
	c_price.append(e)

	df=pd.DataFrame(data)
	df.to_excel("House.xlsx")
	_a=input("Enter '0' to save changes>>>")
	if _a == "0":
		break
	else:
		continue

print(df)