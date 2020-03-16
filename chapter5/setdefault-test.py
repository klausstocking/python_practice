#============setdefault()像是get(),如果鍵遺漏的話,setdefault()會指派給字典=================

big_table = {'a': 1, 'b': 2}
c = big_table.setdefault('c', 3)
print(c)
c
print(big_table)

