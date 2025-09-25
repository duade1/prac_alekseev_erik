import cowsay
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
t = int(input())
l = 0
r = n
b = r // 2
c = True
while l != r-1:
    if a[b] > t:
        r = b
        b = (l + r) // 2
    elif a[b] < t:
        l = b + 1
        b = (l + r) // 2
    if a[b] == t:
        cowsay.cow(b)
        c = False
        break
if c:
    cowsay.cow(-1)
