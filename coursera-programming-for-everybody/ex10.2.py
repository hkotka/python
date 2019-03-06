name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
lst = list()
counts = dict()

for line in fh:
    if line.startswith("From "):
        sline = line.split()
        time = sline[5]
        time = time[0:2]
        if time not in counts:
            counts[time] = 1
        else:
            counts[time] += 1

for key, value in list(counts.items()):
    lst.append((key, value))

lst.sort()

for key, value in lst:
    print(key, value)