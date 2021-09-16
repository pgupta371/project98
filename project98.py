def dataSwipe():
    f1 = input("Enter First File Name: ")
    f2 = input("Enter Second File Name: ")

    with open(f1,"r") as a:
        data_a = a.read()
    with open(f2,"r") as b:
        data_b = b.read()

    with open(f1,"w") as a:
        a.write(data_b)
    with open(f2,"w") as b:
        b.write(data_a)

dataSwipe()
    