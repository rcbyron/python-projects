"""
A simple example of using Python's multiprocessing module
Multiprocessing is basically the same as threading but memory is not shared easily
"""
import multiprocessing as mp
import random
import string

NUM_THREADS = 10

# Define an output queue
output = mp.Queue()


# Define a example function
def rand_string(length):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                    string.ascii_lowercase +
                    string.ascii_uppercase +
                    string.digits)
                    for i in range(length))
    output.put(rand_str)


# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_string, args=[5]) for x in range(NUM_THREADS)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
while not output.empty():
    print(output.get())
