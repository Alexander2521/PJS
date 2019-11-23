# class Starshapeddonut:
#     def __init__ (flavor, strawberry, apple):
#         flavor.straberry = strawberry
#         flavor.apple = apple
#
#     ph1 = Starshapeddonut("John" , "Jack")
#
#     print(ph1.straberry)
#     print(ph1.apple)

class StarShapedDonut:
    def __init__(donut, fruits, topping):
        donut.flavor = fruits
        donut.topping = topping

    def __taste__ (alex):
        print (" I taste like " + alex.flavor)

    def __topping__(Jasmine):
        print("I have " + Jasmine.topping+ " on top")

appleDonut = StarShapedDonut('apple', 'almond')
strawberryDonut = StarShapedDonut('straberry', 'pineapple')
JohnDonut = StarShapedDonut("John's Leg", "John's Eyeballs")

# JohnDonut.__taste__()
strawberryDonut.__topping__()
JohnDonut.__topping__()

print("this donut tastes like " + appleDonut.flavor)
print("this donut has " + strawberryDonut.topping + " on top!")
