a=5
b=10
sum=a+b
#normal formatting
print("Language is {}".format("Python"))
print("Sum of {} & {} is {}".format(a,b,sum))
#index based formatting
print("Sum of {1} & {0} is {2}".format(a,b,sum))
#value based formatting
print("{c} values of vars {c} & {d}".format(c=5,d=10))