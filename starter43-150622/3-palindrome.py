from decimal import Decimal


class input_data:
    def __init__(self, a, b):
        self.a = a
        self.b = b


input_list = []
T = int(input())


def ceildiv(a, b):
    return -(a // -b)


def palindrome(string, n):
    l = len(string)
    if (n == (l * 2)):
        return string + string[::-1]
    else:
        return string + (string[:-1])[::-1]


def process(a, b):
    if b == 1:
        res = ''
        for j in range(1, a+1):
            res += 'a'
        print(res)
    else:
        c = b*2-(b-2)
        if (b == 2 and (c == 3 or c == 4)):
            palindrome("ab", a)
        if ((a == (b*2)) or (a == ((b*2)-1))):
            result = ""
            for i in range(97, 97+b):
                result += chr(i)
                palindrome_str = palindrome(result, a)
            print(palindrome_str)
        else:
            print(-1)


for i in range(1, T+1):
    a, b = input().split()
    data = input_data(int(a), int(b))
    input_list.append(data)

for data in input_list:
    a = data.a
    b = data.b
    process(a, b)
