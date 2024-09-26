
# a = {"h": "Harry",
# 	"from": "India",
# 	"marks": [92,98,96]}

# print(a)
# a.update({"friend_name":"Shivanand"})
# x=input("Enter the key for which you wish to get the value:\t")
# print(a.get(x))
# a["from"]="Singapore"

# print(a)
# print(a.get(x))
# print(a.get("name"))

# if a.get(x)==None:
#     print("this get function is returning nothing, please correct it...!")
# else:
#     print("Hi, ",a.get("name"))


# ___________________________________________________________________

# creating a new dictionary to get the key by providing the values
my_dict ={"java":100, "python":112, "c":11}
print(my_dict)

find=int(input("Enter the code of the language you want to learn : "))

# list out keys and values separately
list_key=list(my_dict.keys())
list_value=list(my_dict.values())

for key,val in my_dict.items():
    if str(val).endswith(str(find)):
        print(key)

print(my_dict.items())

# print(list_key)
# print(list_value)

# pos=list_value.index(find)
# print(list_key[pos])

# print(my_dict.get('java'))
# print(my_dict.get('javascript'))
# print(my_dict['java'])
# print(my_dict['javascript'])




