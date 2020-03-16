class quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'


class questionquote(quote):
    def says(self):
        return self.words + '?'

class exclamationquote(quote):
    def says(self):
        return self.words + '!'

hunter = quote('klaus', "I'm hunting wabbits")
hunter1 = questionquote('stocking', "I'm player")
hunter2 = exclamationquote('james', "I'm joker")
#print(hunter.person)
#print(hunter.words)

print(hunter.who() + " says : " + hunter.says())
print(hunter1.who() + " syas : " + hunter1.says())
print(hunter2.who() + " says : " + hunter2.says())

class babblingbrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
brook = babblingbrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(brook)
