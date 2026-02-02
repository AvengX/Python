try:
    x=int(input("Enter x: "))
    ans=10/x

except ZeroDivisionError:
    print(f"Division by zero is not allowed")

except ValueError:
    print(f"Invalid Input")    

else:
    print(f"ans={ans}")
    