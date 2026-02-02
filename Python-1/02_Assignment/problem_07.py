while True:
    user_input=input("Enter a number (or type 'Quit to stop) :")
    if user_input.lower()=="quit":
        print("Program ended")
        break
    n=float(user_input)
    if n>0:
        print(f"{n} is +ve")
    elif n<0:
        print(f"{n} is -ve")
    else:
        print("Number is zero")        
