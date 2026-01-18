symbols = '$¢£¥€¤'
ascii = [ord(s) for s in symbols
    if ord(s) >127]

ascii_2 = list(filter(lambda c: c > 127, map(ord, symbols)))


print(str(map(ord, symbols)))

print(ascii,"-------", ascii_2)