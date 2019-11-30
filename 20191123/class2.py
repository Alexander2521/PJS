class Donut :
    def __init__(self, shape, color, calories):
        self.shpe = shape
        self.color = color
        self.calories = calories

    def die(self):
        if(self.calories>15000):
            print("you're dead")
        else:
            print("you're not dead yet. you have the perfect amount of insulin, to regulate homeostasis")

        
class StarShapedDonut(Donut):
    def __init__(donut, fruits, topping, color, calories, shape = 'star'):
        super().__init__( shape , color, calories)
        # donut.shape = "star" this is wrong!
        donut.flavor = fruits
        donut.topping = topping

    def __taste__ (alex):
        print (" I taste like " + alex.flavor)

    def __topping__(Jasmine):
        print("I have " + Jasmine.topping+ " on top")

appleDonut = StarShapedDonut('apple', 'almond', 'orange', 20000)
appleDonut.die()
appleDonut.calories = 10000
appleDonut.die()


# strawberryDonut = StarS
hapedDonut('straberry', 'pineapple')
# JohnDonut = StarShapedDonut("John's Leg", "John's Eyeballs")

# JohnDonut.__taste__()
# strawberryDonut.__topping__()
# JohnDonut.__topping__()
#
# print("this donut tastes like " + appleDonut.flavor)
# print("this donut has " + strawberryDonut.topping + " on top!")
