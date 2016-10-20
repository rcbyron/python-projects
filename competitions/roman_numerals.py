from collections import OrderedDict

number = int(input('Enter a number: '))

answer = ''

translate = {'M':  1000,
             'CM': 900,
             'D':  500,
             'CD': 400,
             'C':  100,
             'XC': 90,
             'L':  50,
             'XL': 40,
             'X':  10,
             'IX': 9,
             'V':  5,
             'IV': 4,
             'I':  1}

finished = OrderedDict(sorted(translate.items(),
                              key=lambda t: t[1],
                              reverse=True))

for k, v in finished.items():
    while number-v >= 0:
        number -= v
        answer += k

print(answer)
