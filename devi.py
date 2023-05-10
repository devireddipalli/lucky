x=int(input())
s=0
while x>0:
    r=x%10
    s=s+r
    x=x//10
print(s)
