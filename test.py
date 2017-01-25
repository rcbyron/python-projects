
def fix_time(time='12:00 p.m.'):
    arr = time.strip().replace('.', '').split(":")
    hour = int(arr[0])
    min = int(arr[1][:-3])
    meridian = arr[1][-2:]
    if meridian == "am" and hour is 12:
        hour -= 12
    if meridian == "pm" and hour is not 12:
        hour += 12
    return '{:02d}:{:02d}:00'.format(hour, min)


print(fix_time('12:00 a.m.'))
print(fix_time('1:00 a.m.'))
print(fix_time('12:45 p.m.'))
print(fix_time('1:30 p.m.'))