#======================python命名規範(__)=========================
class duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name
    
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = duck('klaus')
print(fowl.name)

fowl.name = 'momiji'
print(fowl.name)

print(fowl._duck__name)
