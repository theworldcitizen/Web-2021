a = int(input())
b = int(input())

for i in range(a, b + 1):
    if(i**(1/2) == round(i**(1/2))):
        print(i, end=" ")