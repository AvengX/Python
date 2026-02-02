nums=(1,2,3,4,5,6,7,8,9)
even_list=[]
odd_list=[]
for x in nums:
        if x%2==0:
            even_list.append(x)
        else:
            odd_list.append(x)    
print(tuple(even_list))
print(tuple(odd_list))