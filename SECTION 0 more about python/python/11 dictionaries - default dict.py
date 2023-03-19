#to activate virtual env : source venv/bin/activate

""" 
  dict() : it method creates an dictionary
 """

# from io import open
import pathlib
from collections import defaultdict

route = str(pathlib.Path().absolute()) + '/SECTION 0 more about python/python/document.txt'
document = []
with open(route) as f:
  document = f.readlines()
  print(document)
    

word_counts = {}
for word in document:
  if word in word_counts:
    word_counts[word] += 1
  else:
    word_counts[word] = 1

print(word_counts)

word_counts = {}
for word in document:
  try:
    word_counts[word] += 1
  except KeyError: # if we use defaultdict, it never will trown an KeyError
    word_counts[word] = 1
print(word_counts)


word_counts = {}
for word in document:
  previous_count = word_counts.get(word, 0) # get(word, 0) : if word doen't exists return 0
  print('-------previous_count', previous_count)
  word_counts[word] = previous_count + 1
print(word_counts)

# ------------------------------------------- using defaultdict
""" 
  The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
 """
word_counts = defaultdict(int) # int() produces 0
for word in document:
  word_counts[word] += 1
print(word_counts)

# dicts can also be useful with list or dict, or even your own functions:
dd_list = defaultdict(list) # list() produces an empty list
dd_list[2].append(1) # now dd_list contains {2: [1]}
print('----dd_list', dd_list)
dd_dict = defaultdict(dict) # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle" # {"Joel" : {"City": Seattle"}}
print('----dd_dict', dd_dict)
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1 # now dd_pair contains {2: [0, 1]}
print('----dd_pair', dd_pair)

