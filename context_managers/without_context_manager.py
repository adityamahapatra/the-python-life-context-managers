file_ = open("/home/aditya/Desktop/sample.txt", "r")
try:
    lines = file_.readlines()
    for line in lines:
        print(line)
finally:
    file_.close()
