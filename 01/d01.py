import re

if __name__ == "__main__":

    pattern = re.compile(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))")
    translate = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
                 '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

    with open("input.txt") as input:
        sum = 0
        for l in input:
            print(l)
            matches = pattern.findall(l)
            print(matches)
            digits = [translate[m] for m in matches]
            print(digits)
            print('\n')
            val = digits[0] * 10 + digits[-1]
            sum += val
        print(sum)