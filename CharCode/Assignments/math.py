# convert to binary
def toBinary(n):
    if n > 1:
        toBinary(n // 2)
    print(n % 2, end='')


toBinary(10)


# convert to hex
def toHex(n):
    if n > 1:
        toHex(n // 16)
    print(n % 16, end='')


toHex(11)
