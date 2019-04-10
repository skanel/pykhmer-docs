#Read file
open_file = open("E:\\DOCUMENT\\Lecture\\pykhmer-docs\\phonebook.txt")
d = {}
with open_file as f:
    #read file
    lines = f.readlines()
    #print(lines)
    for line in lines:
        l = line.split(": ")
        d[l[0]] = l[1]

print(d["Mr.A"])
