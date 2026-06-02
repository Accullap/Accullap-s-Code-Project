def binary_to_dec(stringbinary):
    decimal = 0
    for digits in stringbinary:
        decimal = decimal * 2 + int(digits)
    return decimal

result = binary_to_dec("10011111111")

print(result)