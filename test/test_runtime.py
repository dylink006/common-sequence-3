import random
import string
import time
import sys
sys.path.append("../")
from src.hvlcs import hvlcs
import matplotlib.pyplot as plt

def main():
    k = 26
    values = {}
    string_lengths = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]

    for c in string.ascii_lowercase:
        values[c] = random.randint(1, 10)

    length_to_time = {}

    for sl in string_lengths:
        string1 = ""
        string2 = ""
        for i in range(sl):
            string1 += chr(random.randint(97, 122))
            string2 += chr(random.randint(97, 122))
        
        start = time.perf_counter()
        val, seq = hvlcs(string1, string2, values)
        end = time.perf_counter()

        length_to_time[sl] = end - start

        print(val)
        print(seq)

    plt.plot(length_to_time.keys(), length_to_time.values())
    plt.title("Runtime vs String Length")
    plt.xlabel("String Length")
    plt.ylabel("Runtime")
    plt.savefig('runtime_vs_string_length.png')
    plt.show()

if __name__ == '__main__':
    main()