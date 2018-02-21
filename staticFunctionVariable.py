# How to do static function variables in Python

def inc():
    # Because functions are object, we create a property with a dot access (inc.counter)
    inc.counter = getattr(inc, "counter", 0)
    # We increment the counter by one
    inc.counter += 1
    # we return the counter
    return inc.counter

for _ in range(10):
    print(inc(), end=' ')
print()

# Now lets look at the problem of creating a random sequence that does not locally repeat.
   # 1 2 3 2 8 1 8 6 6 8 << bad since 2, 8, 6 repeat too close together
   # 1 2 9 8 1 2 7 4 3  << ok closest repeats are separated by three numbers


from random import sample, randint

def seq():
    """ return next random n """
    seq.last3 = getattr(seq, "last3", sample(range(1, 11), 3))
    i = randint(1, 10)
    while i in seq.last3: # find i not last 3
        i = randint(1, 10)
    seq.last3.append(i) # update history
    seq.last3.pop(0)
    return i

for _ in range(36):
    print(seq(), end= ' ')
    print()