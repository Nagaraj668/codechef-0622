class input_data:
    def __init__(self, a, b):
        self.a = a
        self.b = b


input_list = []
T = int(input())


def process(a, b):
    i = 1
    while a < b:
        a = a + i
        if (a == b):
            print("yes")
            break
        else:
            if (i == 1):
                i = 2
            else:
                i = 1
    else:
        print("no")


for i in range(1, T+1):
    a, b = input().split()
    data = input_data(int(a), int(b))
    input_list.append(data)

for data in input_list:
    a = data.a
    b = data.b
    process(a, b)
