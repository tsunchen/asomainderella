
def chunkschop(lst: list, n:int = 1):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(sample)
print(list(chunkschop(sample, 3)))
print(list(chunkschop(sample, 2)))
print(list(chunkschop(sample)))

 