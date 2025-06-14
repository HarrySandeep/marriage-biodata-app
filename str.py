string="My name is Sandeep"

str=string.split(" ")
#print(str)
new_str=[]

for name in str:
    new_str.append(name[::-1])
#print(new_str[::-1])

str1="Python and Data Science"
str2=str1.lower().split(" ")
print(str2)
vowel=["a","e","i","o","u"]

for val in str2:
    for i in vowel:
        if i not in val:
            str2.remove(i)
            
   