from decimal import Decimal
class input_data:
    def __init__(self, a, b):
        self.a = a
        self.b = b


input_list = []
T = int(input())


def process(a, b):
    i = 1
    n = ((b-a)+1)/3
    if (Decimal(n) % 1 == 0):
        print("no")
    elif n == 1:
        print("yes")
    else:
        print("yes")


for i in range(1, T+1):
    a, b = input().split()
    data = input_data(int(a), int(b))
    input_list.append(data)

for data in input_list:
    a = data.a
    b = data.b
    process(a, b)
