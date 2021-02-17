string = input()

for i in string:

    if i == "c=":
        i = string.replace(i, "A")
        print("check1")
    if i == "c-":
        i = string.replace(i, "B")
        print("check2")

    if i == "dz=":
        i = string.replace(i, "C")
        print("check3")

    if i == "d-":
        i = string.replace(i, "D")
        print("check4")

    if i == "lj":
        i = string.replace(i, "E")
        print("check5")

    if i == "nj":
        i = string.replace(i, "F")
        print("check6")

    if i == "s=":
        i = string.replace(i, "G")
        print("check7")

    if i == "z=":
        i = string.replace(i, "H")
        print("check8")


print(string)

print(len(string))