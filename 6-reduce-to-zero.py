import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


class input_data:
    def __init__(self, a, b):
        self.a = a
        self.b = b


input_list = []
T = int(input())


def process(a, b):
    if a == b:
        print(a)
    elif a == 0 or b == 0:
        print(-1)
    else:
        if a > b:
            a, b = b, a

        count = 0
        while a < b:
            a *= 2
            count += 1

        print(count + b)


for i in range(1, T+1):
    a, b = input().split()
    data = input_data(int(a), int(b))
    input_list.append(data)

for data in input_list:
    a = data.a
    b = data.b
    process(a, b)
