import math
n = int(input("Введите число: "))
a = []
for i in range(1, n+1):
    print(i, sep=" ",end=" ")
    if(i < n):
        print("*",sep=" ", end=" ")
    a.append(i)
print("=", math.prod(a))