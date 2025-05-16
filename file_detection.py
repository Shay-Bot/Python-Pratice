# Python file detection

import os

file_path = "py/file/file.txt"

if os.path.exists(file_path):
    print(f"the loaction '{file_path}' exists ")
    if os.path.isfile(file_path):
        print("Yes")
    else: 
        print("No")
else:
    print("not")