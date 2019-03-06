c = {'a':22, 'b':1, 'k':99, 'v':42}
tmp = list()
for key, value in c.items():
    tmp.append((value, key))

tmp = sorted(tmp, reverse=True)
print(tmp)