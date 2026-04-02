from hvlcs import hvlcs
import sys

def main(filepath):
    try:
        with open(filepath, 'r') as f:
            line1 = f.readline().split()
            if not line1:
                raise ValueError("Missing k")
            if len(line1) != 1:
                raise ValueError("First line must contain only integer k")
            k = line1[0]
            if not k.isdigit():
                raise ValueError("k must be an integer")
            k = int(k)

            values = {}
            for i in range(k):
                line = f.readline().split()
                if not line:
                    raise ValueError(f"Missing value line {i + 1}")
                if len(line) != 2:
                    raise ValueError(f"Value line {i + 1} must contain a character and an integer")
                c = line[0]
                n = line[1]
                if len(c) != 1:
                    raise ValueError(f"Key on line {i + 1} must be a single character")
                if not n.isdigit():
                    raise ValueError(f"Value on line {i + 1} must be a positive integer")
                values[c.lower()] = int(n)
            
            string1line = f.readline().split()
            if not string1line:
                raise ValueError("Missing first string")
            if len(string1line) != 1:
                raise ValueError("First string line must contain only one string")
            string1 = string1line[0]
            if not string1.isalpha():
                raise ValueError("First string contains non-alphabetic characters")
            string1 = string1.lower()
            if any(char not in values for char in string1):
                raise ValueError("First string contains characters not in values dictionary")
            
            string2line = f.readline().split()
            if not string2line:
                raise ValueError("Missing second string")
            if len(string2line) != 1:
                raise ValueError("Second string line must contain only one string")
            string2 = string2line[0]
            if not string2.isalpha():
                raise ValueError("Second string contains non-alphabetic characters")
            string2 = string2.lower()
            if any(char not in values for char in string1):
                raise ValueError("Second string contains characters not in values dictionary")
            
            val, seq = hvlcs(string1, string2, values)
            print(val)
            print(seq)
    except FileNotFoundError:
        print("Bad file path, file does not exist.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            main(arg)
    else:
        print("No filepath given. Usage: python3 main.py <filename1> <optional filenames...>")