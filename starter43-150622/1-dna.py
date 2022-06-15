class input_data:
    def __init__(self, n, x):
        self.n = n
        self.x = x


T = int(input())
data_list = []
for i in range(1, T+1):
    N = int(input())
    X = input()
    subs = input_data(N, X)
    data_list.append(subs)

for sub in data_list:
    result = ""
    string = sub.x
    i = 0
    while i < (sub.n):
        if (i >= len(string)):
            break
        bin = string[i]+string[i+1]
        if bin == "00":
            result += "A"
        elif bin == "01":
            result += "T"
        elif bin == "10":
            result += "C"
        elif bin == "11":
            result += "G"
        i += 2
    print(result)
