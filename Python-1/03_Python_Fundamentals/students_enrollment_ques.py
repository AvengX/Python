''' Student Enrollment
. List all unique courses
.list students enrolled in english
.create dictionary(Student,set of courses)'''
info=[
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

# print(len(info))
# for name,course in info:
#     print(name,course)
# for i in info:
#     print(i)

# List all unique courses
courses_set=set()
for tup in info:
    courses_set.add(tup[1])
print(courses_set)    


#list students enrolled in english
for name,course in info:
    if(course=="English"):
        print(name)


#create dictionary(Student,set of courses)
dict={}
for name,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)            
