def from_dec(num, new_base):
    answer = 0
    count = 0
    while num > 0:
        answer += num % new_base * (10 ** count)
        count += 1
        num //= new_base
    return answer


def to_dec(num, old_base):
    answer = 0
    count = 0
    while num > 0:
        answer += num % 10 * (old_base ** count)
        count += 1
        num //= 10
    return answer

while True:
    old_base = int(input('From Base: '))
    new_base = int(input('To Base: '))
    num_str = input('Number: ')
    num = float(num_str)

    if old_base > 10 or new_base > 10:
        print('\nI can\'t handle bases greater than 10 at the moment.\n')
        continue

    error = False
    for c in str(num_str):
        if int(c) >= old_base:
            error = True
            break

    if error:
        print('Danger, DANGER Will Robinson! Invalid Number!')
    else:
        if old_base is 10:
            answer = from_dec(num, new_base)
        elif new_base is 10:
            answer = to_dec(num, old_base)
        else:
            answer = from_dec(to_dec(num, old_base), new_base)
        print('Answer: %.1f\n' % answer)
