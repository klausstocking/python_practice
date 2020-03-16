#繼承
class Car():
    def exclaim(self):
        print("I am a car")
class Yugo(Car):
    def exclaim(self):
        print("I am Yugo! Musch like Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()
