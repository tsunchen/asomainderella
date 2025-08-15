from collections import deque

def roundrobin(*iterables):
    """
    Round Robin
    """
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # remove an exhausted iterator
            iterators.popleft()


print(list(roundrobin(['Alpha', 'Beta', 'Gama', 'Delta', 'elapse', 'fiza'])))
# print(list(roundrobin(['Alpha', 'Beta', 'Gama'], 'Delta', ['elapse', 'fiza'])))
# print(list(roundrobin(['a', 'B', 'c'], 'd', ['e', 'F'])))
# print(list(roundrobin('aBc', 'd', 'eF')))
