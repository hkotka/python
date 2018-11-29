def computepay(h, r):
    overtime = 0
    if h > 40:
        overtime = h - 40
    total = (h - overtime) * r + (overtime * (r * 1.5))
    return total

hrs = input("Enter Hours:")
rate = input("Enter your rate:")
p = computepay(float(hrs), float(rate))

print("Pay",p)