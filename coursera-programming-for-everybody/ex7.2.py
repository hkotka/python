# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        score = float(line[20:])
        total = total + score

avgscore = total / count
print("Average spam confidence:", avgscore)