import json

data={
    "name":"Ayish",
    "age":33,
    "isteach":True
}
# with open("data.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)
with open("data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)