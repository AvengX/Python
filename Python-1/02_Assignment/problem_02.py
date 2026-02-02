def even(a,b):
    start=min(a,b)
    end=max(a,b)
    print(f"Even numbers between {a} and {b} are:")
    for i in range(start,end+1):
        if(i%2==0):
            print(i,end=" ")            
even(1,10)        
             