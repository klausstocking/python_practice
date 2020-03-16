#=========================super()呼叫父類別===============================
#class person():
#    def __init__(self, name):
#        self.name = "name : " + name
#
#class emailperson(person):
#    def __init__(self, name, email):
#        super().__init__(name)
#        self.email = "email : " + email
#
#bob = emailperson('bob frapples', 'bob@gmail.com')
#
#print(bob.name)
#print(bob.email)



#========================getter & setter=================================
#class duck():
#    def __init__(self, input_name):
#        self.hidden_name = input_name
#
#    def get_name(self):
#        print('inside the getter')
#        return self.hidden_name
#
#    def set_name(self, input_name):
#        print('inside the setter')
#        self.hidden_name = input_name
#
#    name = property(get_name, set_name)
#
#test = duck('klaus')
#print(test.name)
#
#test.name = 'momiji'
#print(test.name)



#=============================裝飾器======================================
class duckat():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setting')
        self.hidden_name = input_name


fowl = duckat('james')
print(fowl.name)

fowl.name = 'stocking'
print(fowl.name)
