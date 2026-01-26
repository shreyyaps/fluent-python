colors = ['black', 'white']
sizes = ['S','M','L']
tshirts = [[color,size] for color in colors
                             for size in sizes]

print(tshirts)

# this is same as this 

for color in colors:
    for size in sizes:
        print([color,size])


for tshirt_exp in ((c,s) for c in colors for s in sizes):
    print(tshirt_exp)