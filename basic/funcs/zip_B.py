for i in zip([1, 2, 3], ['a',  'b', 'c']):
    print(i)

print(dict(zip([1, 2, 3], range(5))))  # {1: 0, 2: 1, 3: 2}

segments = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(segments[:3] + segments[-3:])

AS = []
a1 = [[1, 2]]
a2 = [[2, 3]]
AS.extend(a1)
AS.extend(a2)
print(AS)
