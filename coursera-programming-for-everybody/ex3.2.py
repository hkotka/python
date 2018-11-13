hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter your rate:")
r = float(rate)
baserate = 40.0

if h > baserate:
    overtime = h - baserate
    pay = baserate * r + overtime * r * 1.5
else:
    pay = h * r

print(pay)