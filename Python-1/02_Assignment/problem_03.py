def print_digit(n):
    if n==0:
        print(0)
        return 
    while n>0:
       digit=n%10
       print(digit)
       n=n//10   

print_digit(10)        