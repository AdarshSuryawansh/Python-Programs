
# Python generator

def my_gen():
    yield "A"
    yield "B"
    yield "c"

g = my_gen() # generator object

print(next(g))
print(next(g))
print(next(g))

print(next(g)) ##This will produce an stop iteration error becoz no next element is avaliable