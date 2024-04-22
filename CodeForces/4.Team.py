n = int(input())
res=0


for i in range(n):
    a, b, c= map(int, input().split())
    if ((a+b+c) >= 2):
        res+=1

print(res)

# for i in range (n):
#     x = str(input())
#     if "1 1" in x:
#         c+=1
#     elif "1 0 1" in x:
#         c+=1

# print(c)