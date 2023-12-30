def trebuchet(s: str) -> int:
    digits_as_str = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    print(s)
    print(len(s))
    digits = []
    for i, c in enumerate(s):
        if c.isdigit():
            digits.append(c)
        else:
            for d in digits_as_str:
                j = i + 1
                while d.startswith(s[i:j]) and j <= len(s):
                    if len(s[i:j]) == len(d):
                        digits.append(digits_as_str.index(d) + 1)
                        break
                    j += 1

    if len(digits) == 1:
        res = f'{digits[0]}{digits[0]}'
    else:
        res = f'{digits[0]}{digits[-1]}'
    print(digits)
    return int(res)


if __name__ == '__main__':
    total: int = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            calc = trebuchet(s=line)
            print(f"line: {line}, calculation: {calc}")
            total += calc
    print(total)
