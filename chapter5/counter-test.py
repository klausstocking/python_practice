#==============counter_test====================

from collections import Counter
word = ['a', 'b', 'a', 'b', 'a']
word_counter = Counter(word)
print(word_counter)

#================_1_==========================

lunch = ['a', 'b', 'a']
lunch_counter = Counter(lunch)
print(lunch_counter)
print(word_counter + lunch_counter) #add

print(word_counter & lunch_counter)
