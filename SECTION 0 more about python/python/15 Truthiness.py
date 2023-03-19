#Python uses the value None to indicate a nonexistent value. It is similar to other languages’ null:

x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"


""" 
  * all these values is threaded as False by Python
    - False
    - None
    - [] (an empty list)
    - {} (an empty dict)
    - ""
    - set()
    - 0
    - 0.0
 """

def some_function_that_returns_a_string():
  return

s = some_function_that_returns_a_string() #in the conditional will be threated as false
first_char = None
print('-----first_char', first_char) 
if s: 
  first_char = s[0]
else:
  first_char = ""
print('-----first_char', first_char) 

first_char = s and s[0]
print('-----first_char', first_char) 



# --------------- using Truthiness
# all() function, which takes an iterable and returns True precisely when every element is truthy
# any() function, which returns True when at least one element is truthy
res = all([True, 1, {3}]) # True, all are truthy
print('-----res', res) 
res = all([True, 1, {}]) # False, {} is falsy
print('-----res', res) 
res = any([True, 1, {}]) # True, True is truthy
res = all([]) # True, no falsy elements in the list
print('-----res', res) 
res = any([]) # False, no truthy elements in the list
print('-----res', res) 
