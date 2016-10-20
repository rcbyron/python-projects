""" Prints the "Two's Complement" (negative) of a number """

num = input('Enter a binary number: ')
answer = ''
hit_one = False

for c in reversed(num):
    if c == '0':
        answer += '0' if not hit_one else '1'
    else:
        if not hit_one:
            hit_one = True
            answer += '1'
        else:
            answer += '0'

print('2\'s Complement: ', answer[::-1])
