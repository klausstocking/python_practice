class a():
    count = 0
    def __init__(self):
        a.count += 1
    def exclaim(self):
        print("I'm an a")
    @classmethod
    def kids(cls):
        print("a has", cls.count, "little object")

easy_a =a()
breezy_a = a()
wheezy_a = a()
a.kids()
