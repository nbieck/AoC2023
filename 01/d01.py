if __name__ == "__main__":
    with open("input.txt") as input:
        sum = 0
        for l in input:
            digits = [ord(c) - ord('0') for c in l if c in "0123456789"]
            val = digits[0] * 10 + digits[-1]
            sum += val
        print(sum)