digit = [4, 5, 6]

num = int(''.join(map(str, digit)))
    # Increment the integer by 2
num += 2

res = str(num)
finalRes = [int(digit) for digit in res]

print(finalRes)