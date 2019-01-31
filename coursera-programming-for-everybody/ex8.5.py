fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    sline = line.split()
    if 'From:' in sline:
        count = count + 1
        lst.append(sline[1])

i = -1
for item in lst:
    i = i + 1
    print(lst[i])

print("There were", count, "lines in the file with From as the first word")