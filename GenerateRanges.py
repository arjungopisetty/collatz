def cycle_length (n) :
    c = 1
    while n > 1:
        if n & 1 == 0:
            n = (n >> 1)
        else:
            n = (n << 1) + n + 1
        c += 1
    assert c > 0
    return c

max_length = 0
set = []

for i in range(1, 5000000):
    length = cycle_length(i)
    if length >= max_length:
        max_length = length
        set.append(i);
print(set)
