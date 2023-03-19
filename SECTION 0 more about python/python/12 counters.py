import pathlib
from collections import defaultdict
from collections import Counter

route = str(pathlib.Path().absolute()) + '/SECTION 0 more about python/python/document.txt'
document = []
with open(route) as f:
  document = f.readlines()
  print(document)


# ---------- Counter: A Counter turns a sequence of values into a defaultdict(int)-like object mapping keys to counts:
c = Counter([0, 1, 2, 0]) # c is (basically) {0: 2, 1: 1, 2: 1}

word_counts = Counter(document)
print('----word_counts', word_counts)

# A Counter instance has a most_common method that is frequently useful:
res = word_counts.most_common(3) #return the 3 most common word and its counts 
print('----res', res)

