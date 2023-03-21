

var1 = [2, 2, 1]
ht1 = {}
for item in var1:
    if item not in ht1:
        ht1[item] = 1
    else:
        ht1[item] += 1

for k in ht1:
    if ht1[k] == 1:
        print(k)