# Link: https://codeforces.com/contest/677/problem/A

n, h = map(int, input().split())

numbers = list(map(int, input().split()))

output = 0

for nunber in numbers:
    
    if nunber <= h :
        output += 1
    
    if nunber > h :
        output += 2

print(output)