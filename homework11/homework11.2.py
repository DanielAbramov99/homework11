information: str = "Daniel Abramov from Eilat"
print("length:", len(information))
print("uppercase:", information.upper())
print("lowercase:", information.lower())
print("start with first name:", information.startswith("Daniel"))
print("end with city:", information.endswith("Eilat"))
splits: list[str] = information.split()
print(splits)
stars = information.replace(" ", "*")
print(stars)
print("centered:", information.center(50, "="))
print("from 4th letter:", information[3:len(information)])
print("first four letters:", information[0:4])
print("all first letters are capital:", information.title())
even1: list[str] = [char for char in information if not char.isspace()]
print(even1)
print("only even", even1[1::2])  # first way
even = information.replace(" ", "")
print("only even letters:", even[1::2])  # second way
