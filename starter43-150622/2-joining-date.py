from decimal import Decimal
class input_data:
    def __init__(self, a, b):
        self.a = a
        self.b = b


input_list = []
T = int(input())

def ceildiv(a, b):
    return -(a // -b)

def process(a, b):
    sets = ceildiv(a,5)
    c = (sets - ((b-1) // 5)) - 1
    print(c)


for i in range(1, T+1):
    a, b = input().split()
    data = input_data(int(a), int(b))
    input_list.append(data)

for data in input_list:
    a = data.a
    b = data.b
    process(a, b)
