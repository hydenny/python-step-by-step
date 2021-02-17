string = input()

count = len(string)

if "c=" in string:
    count -= string.count("c=")
   
if "c-" in string:
    count -= string.count("c-")

if "dz=" in string:
    count -= string.count("dz=")

if "d-" in string:
    count -= string.count("d-")

if "lj" in string:
    count -= string.count("lj")

if "nj" in string:
    count -= string.count("nj")

if "s=" in string:
    count -= string.count("s=")

if "z=" in string:
    count -= string.count("z=")

print(count)
