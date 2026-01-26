symbols = '$¢£¥€¤'
yo = tuple(ord(symbol) for symbol in symbols)
print(yo)
import array

hey = array.array('I',(ord(symbol) for symbol in symbols))

print(hey)

