import math


class input_data:
    def __init__(self, a, b):
        self.a = a
        self.b = b


input_list = []
T = int(input())


def process(a, b):
    z = abs(a-b)
    ans = 0
    i = 1
    while i**2 <= z:
        if z % i == 0:
            ans += 1
            if z//i != i:
                ans += 1
        i = i + 1
    print(ans)


for i in range(1, T+1):
    a, b = input().split()
    data = input_data(int(a), int(b))
    input_list.append(data)

for data in input_list:
    a = data.a
    b = data.b
    process(a, b)
