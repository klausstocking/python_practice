class parent():
    def __init__(self, name):
        self.name = name

class sister(parent):
    def __init__(self, name):
        self.name = "sister " + name

class brother(parent):
    def __init__(self, name):
        self.name = name + " brother"

test_parrent = parent('mon and dad')
test_sister = sister('sting')
test_brother = brother('hongye')

print(test_parrent.name)
print(test_sister.name)
print(test_brother.name)
