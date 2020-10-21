# Replace the file path with an existing text file on your machine.
with open("/home/aditya/Desktop/sample.txt", "r") as file_:
    lines = file_.readlines()
    for line in lines:
        print(lines)
