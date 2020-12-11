
# these allows to insert  quotes in python
text1 = ' "Master" '
text2 = " \"en Python\" "

textJoined = text1 + " " + text2
print(textJoined)
print('-------------------')

#insert line salt
textJoined = text1 + "\n" + text2
print(textJoined)
print('-------------------')

#insert tabulation
textJoined = text1 + "\t" + text2
print(textJoined)
print('-------------------')

#delete the first part of text
textJoined = text1 + "\r" + text2
print(textJoined)