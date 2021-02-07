

# try:
#     file = open("a_file.txt")
#     a_dictonary = {"key":"value"}
#     print(a_dictonary["key"])
# except FileNotFoundError:
#     file.open
#
#
# except KeyError as error_message:
#     print(f"The key {error_message}")
#
# else:



height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height **2
print(bmi)

