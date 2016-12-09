""" A demo of better console output using regex """
import re
import time

from subprocess import Popen, PIPE

SHOW_ORIGINAL_OUTPUT = False

REGEX_OUT = r"(.*)"

pat = re.compile(REGEX_OUT)
orig = time.time()

p = Popen(["python", "company_name_maker.py"], stdout=PIPE)

# Grab stdout line by line as it becomes available.
# This will loop until p terminates.
print("Listening to process...\n")
while p.poll() is None:
    # Blocks until it receives a newline.
    l = str(p.stdout.readline().decode('utf-8'))

    if (SHOW_ORIGINAL_OUTPUT):
        print(l)
    else:
        m = pat.match(l)
        if m is not None:
            print('[{:.2f}] '.format(time.time()-orig) + m.group(1))

# When the subprocess terminates there might be unconsumed output
# that still needs to be processed.
print(p.stdout.read())
