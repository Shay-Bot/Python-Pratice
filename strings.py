# creating strings

name1 = 'me'
name2 = "Kashmir"
name3 = '''us'''

print(name1,name2,name3)   #prints every variable

print(type(name1))        # prints the which type of data type it is

# indexing in a string
print(name2[1])        # prints the alpha on which 1 lies
print(name2[-1])

# traversing a string
for i in name2:         # prints every single letter of the string
     print(i)

# find char/sub string in string
print(name2.find("o"))         # finds if the particular char is present or not in the string

# slicing a string i used to get part of a string
print(name2[1:5])                         # used to print particular part of a string
print(name2[:3])
print(name2[3:])



# converting char to upper case
# str1 = "kashmir"
# str2 = str1.upper()
# print(str2)

# converting char to lower case
# str1 = "KASHMIR"
# str2 = str1.lower()
# print(str2)

# converting first char to sting in upper case
# str1 = "kashmir"
# str2 = str1.capitalize()
# print(str2)

# for removng any trailing space
# str1 = "            kashmir          "
# print(str1.strip())
# print(str1)


# replacings substring
# str1 = "Hello World, World"
# print(str1.replace("World","Earth", 1))

# splliting string
# str1 = "ria sia tia mia jia"
# list = str1.split()   # Gadbad
# print(list)

# concatenation
# str1 = "hello"
# str2 = "world"
# print(str1 + str2)

# fomrat (used to variable value in a string)
# student_name = 'tahir'
# student_marks = 98

# str1 = 'the student name is {s} & marks is {m}'.format(s= student_name, m = student_marks)
# print(str1)

