color=input("Enter your color :")
match color:
    case "Green":
        print("Go")
    case "red":
        print("Stop")
    case "yellow":
        print("Look")
    case _:
        print("Wrong color")        
