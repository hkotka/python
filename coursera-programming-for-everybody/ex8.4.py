fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    splitline = line.split()
    for line in splitline:
        if line not in lst:
            lst.append(line)

lst.sort()
print(lst)
