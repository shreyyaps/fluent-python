import os

co_ordinates = (23.4354, -120.2443)
lat, long = co_ordinates
a = 1
b = 2
a, b = b, a


divmod(20, 8)

t = (20, 8)

divmod(*t)

quotient, remainder = divmod(*t)



path, filename = os.path.split('/home/luciano/.ssh/id_rs')

print(path,"\n", filename)

a, *packed, b, c = range(5)