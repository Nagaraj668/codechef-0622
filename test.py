from sys import stdin
input = stdin.readline
def ii():
    return int(input())

def li():
    return list(map(int, input().split()))

for _ in range(ii()):
    x,y=li()
    if x==y:
        print(x)
        continue

    if x==0 or y==0:
        print(-1)
        continue

    if x>y:
        x,y=y,x

    cnt=0
    while x<y:
        x*=2
        cnt+=1

    print(cnt+y)