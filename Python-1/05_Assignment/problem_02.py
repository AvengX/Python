with open("log.txt","a+")as log:
    log.write("\nmy name is Nikhil")
    log.seek(0)
    content=log.read()
    print(content)
