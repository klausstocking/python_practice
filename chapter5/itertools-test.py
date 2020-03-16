import itertools
for item in itertools.chain(['a', '2'], ['b', '3']):
    print(item)


for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

def multiply(a, b):
    return a* b
for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
