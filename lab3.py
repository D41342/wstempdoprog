x = int (input ("Persze liczbe"))
y = int (input ("Druge liczbe"))

while x < y:
    k = range(x, y)
    break
else:
    k = range(y, x)

for u in k:
    print(u)



