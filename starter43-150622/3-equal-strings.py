class input_data:
    def __init__(self, n, a, b):
        self.n = n
        self.a = a
        self.b = b


input_list = []
T = int(input())


def loop_all(a, b):
    non_matching = set()
    count = 0
    for i in range(0, len(b)):
        if b[i] != a[i]:
            ascii_sum = ord(b[i])
            non_matching.add(ascii_sum)
        
    print(len(non_matching))


for i in range(1, T+1):
    n = input()
    a = input()
    b = input()
    data = input_data(n, a, b)
    input_list.append(data)

for data in input_list:
    c = data.a
    d = data.b
    loop_all(c, d)
