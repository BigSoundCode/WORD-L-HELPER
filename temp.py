original = open("5letterwords.txt", "r")
new = open("newwords.txt", "w")

for line in original:
    line = line.lstrip()
    line = line.upper()
    new.write(line)

original.close
new.close