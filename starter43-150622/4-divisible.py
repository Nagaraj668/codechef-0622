class input_data:
    def __init__(self, a):
        self.a = a


input_list = []
T = int(input())


def process(a):
    list = []
    output = ""
    i = 1
    n = a
    while True:
        list.append(n)
        if n != i:
            list.append(i)
        n = n - 1
        i = i + 1
        if ((i-n) == 2 or (i-n) == 1):
            break
    
    for j in range(len(list)-1, -1, -1):
        output = output + str(list[j]) + " "
    output = output.strip()
    print(output)


for i in range(1, T+1):
    a = int(input())
    data = input_data(a)
    input_list.append(data)

for data in input_list:
    a = data.a
    process(a)
