import array as arr
n = int(input())
a = []
a = input().split(" ")
ans = 0
for i in range(1, n-1):
    if(int(a[i]) > int(a[i-1]) and int(a[i]) > int(a[i+1])):
        ans += 1
print(ans)