#!C:\Users\ADITYA\AppData\Local\Programs\Python\Python36-32\python.exe  

print("Content-Type: text/html")
print()

def findit(x,y):
	if x>y:
	    num=y
	else:
	    num=x
	for i in range(1,num+1):
	    if x%i==0 and y%i==0:
			    hcf=i
	print(hcf)
findit(4,8)
