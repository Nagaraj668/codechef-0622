class subscription:
    def __init__(self, n, x):
        self.n = n
        self.x = x

T = int(input())
subscription_list = []
for i in range(1, T+1):
    the_string = input()
    N, X = the_string.split()
    N = int(N)
    X = int(X)
    subs = subscription(N, X)
    subscription_list.append(subs)

for sub in subscription_list:
    N = sub.n
    X = sub.x
    a = int(N / 6)
    b = N % 6

    if b != 0:
        a = a + 1
    print(a * X)
print()
