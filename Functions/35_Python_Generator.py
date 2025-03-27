
# create the generator function which print he sequence of number

def firstNNumber(num):
    i = 0
    while i <= num:
        yield i
        i += 1


g = firstNNumber(10)

while True:
    print(next(g)) # Will get an error at end of sequence

# to resolve this we will use the for loop
for i in g:
    print(i)

