score = input("Enter Score: ")
try:
    s = float(score)
except:
    s = -1.0

if s == -1.0:
    print("Input not valid")
elif s > 1.0 or s < 0.0:
    print("Not a valid score. Score needs to be between 0.0 and 1.0")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")