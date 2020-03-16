#========defaultdict==============
#============_1_==================
from collections import defaultdict
big_table = defaultdict(int)
big_table['a'] = 1
print(big_table['d'])

print(big_table)

#=============_2_=================
def no_idea():
    return 'Huh?'
name_list = defaultdict(no_idea)
name_list['A'] = 'apple'
name_list['B'] = 'banana'
print(name_list['A'])
print(name_list['B'])
print(name_list['C'])

#=============_3_==================
word_counter = defaultdict(int)
for word in ['a', 'b', 'a', 'a', 'b', 'b', 'a']:
    word_counter[word] += 1
for word, count in word_counter.items():
    print(word, count)


#=============_4_=================

word2_counter = {}
for word2 in ['a', 'a', 'a', 'b', 'b', 'a']:
    if not word2 in word2_counter:
        word2_counter[word2] = 0
    word2_counter[word2] += 1
for word2, count2 in word2_counter.items():
    print(word2, count2)


