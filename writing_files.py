# Python writing files (.txt, .json, .csv)
import json
import csv

# txt_data = "I love Chicken🍗"

# file_path = "output.txt"

# with open(file= file_path, mode= "w") as file:         [w writes the data or overwrite on an existing file]
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")

# try:
#     with open(file= file_path, mode= "x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")


# with open(file= file_path, mode= "a") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")





# .json files

# employee = {
#     "name": "Tahir",
#     "age": 20,
#     "job": "manager"
# }

# file_path = "output.json"

# with open(file= file_path, mode= "w") as file:
#     json.dump(employee, file, intend=4)
#     print(f"txt file '{file_path}' was created")


# .csv files

employees = [
            ["Name", "Age", "Job"],
            ["Tahir", 20, "Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]
]

file_path = "output.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
print ("csv file '{file_path}' uas created")

