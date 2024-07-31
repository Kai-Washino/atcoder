a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for i in range(a):
    if 500 * i > x:
        break
    for j in range(b):
        if 500 * i + 100 * b > x:
            break
        for k in range(c):
            coin = 500 * i + 100 * j + 50 * k
            if coin > x:
                break
            if coin == x:
                count += 1

print(count)