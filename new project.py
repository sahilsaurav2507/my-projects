#hey sahil saurav you are 19 years old
f_name = 'sahil'
l_name = 'saurav'
age = 19

#way 1
print("hey " + f_name + "" + l_name + ",you're " +str(age ) +"years old.")
#way 2
print(f"hey {f_name} {l_name},you're {age} years old")
#way 3
print("hey {} {} ,you're {} years old.".format(f_name, l_name, age))
#way 4
print("hey", f_name, l_name, "you're" , age, "years old.")

example=("hey", f_name, l_name, "you're" , age, "years old.")

print(type(example))