# tuples as records 

lax_cordinates = (33.353456,-118.34645)
city, year, pop, chg, area = ('Tokyo',2003, 32_450, 0.66, 8094)

print(type(59_3))

traveler_ids = [('USA', '31195855'), ('BRA','CE342567'),
('ESP', 'XDA205856')]

for country, num in sorted(traveler_ids):
    print(country+"/"+num) # type: ignore



# tuples as immutable lists

a = (10,'shrey', [1,2])
b = (10, 'shrey', [1, 2])
b=a
a[-1].append(99)
print(a==b)


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = ((1,2),)
tm = ([1,2],)

print(fixed(tf))
print(fixed(tm))
# page 34