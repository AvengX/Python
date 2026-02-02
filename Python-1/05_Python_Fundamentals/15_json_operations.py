import json

py_obj={
    "name":"Ayish",
    "isMR":True
}
# json_str='{"name":"Ayush","IsTeacher":true}'

# py_obj=json.loads(json_str)
json_str=json.dumps(py_obj)
# print(type(py_obj),py_obj)
print(type(json_str),json_str)