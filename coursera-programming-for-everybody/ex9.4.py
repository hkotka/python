fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
count = dict()

for line in fh:
    sline = line.split()
    if 'From:' in sline:
        count[sline[1]] = count.get(sline[1],0) + 1

deco = [(v, k) for (k, v) in count.items()]
_, key = max(deco)

print(key, max(count.values()))
