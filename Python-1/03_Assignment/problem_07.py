string=input("Enter a string :")
count=0
for i in string:
    if(i==" "):
        count+=1
if count>0:
    print(count)
else:
    print("No spaces found")    