f=open("sample.txt","r")

data=f.readline()
print(type(data),data)

data=f.readline()
print(type(data),data)

f.close()