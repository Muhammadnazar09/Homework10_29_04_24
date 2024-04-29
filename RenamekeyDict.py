# my_dict={
#     "name":"Kelly",
#     "age":25,
#     "salari":8000,
#     "sity":"New Yourk"
# }
# my_dict["location"]=my_dict["sity"]
# del my_dict["sity"]
# print(my_dict)

my_dict={
    "name":"Kelly",
    "age":25,
    "salari":8000,
    "sity":"New Yourk"
}
my_dict["location"]=my_dict.pop("sity")
print(my_dict)