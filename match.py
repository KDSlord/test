string = input("enter string: ")
str_to_find = input("enter which to find: ")
x = string.find(str_to_find)
#if character not found
if(x == -1):
    print("enter correct string to find")
else:
    print(x)