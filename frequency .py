53.Count the frequency of elements in a list using a dictionary.

import collections

random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']

frequency = collections.Counter(random_list)
print(dict(frequency))
{'A': 3, 'B': 3, 'C': 1, 'D': 2}
