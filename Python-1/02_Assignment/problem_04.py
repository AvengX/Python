def print_count(n):
    if n==0:
        return 1
    count=0
    n=abs(n)
    while(n>0):
       n=n//10
       count+=1
    return count
print(print_count(23232))                  
