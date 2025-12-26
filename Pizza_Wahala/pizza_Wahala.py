




import math


number_Of_Guests = int(input("Enter The Number of Guests: "))
pizza_Type = input("Enter The Type of Pizza: ")

match pizza_Type:
        case ("Sapa Size"):
            number_Of_Slices = 4
            price_Per_Box = 2000

        case("Small Money"):
            number_Of_Slices = 6
            price_Per_Box = 2400

        case("Big Boys"):
            number_Of_Slices = 8
            price_Per_Box = 3000

        case("Odogwu"):
            number_Of_Slices = 12
            price_Per_Box = 4200

        case(" "):
            print("Invalid Order")
            exit()



number_Of_Boxes = math.ceil(number_Of_Guests/number_Of_Slices)
price = (number_Of_Boxes * price_Per_Box)
remaining_Slice = (number_Of_Boxes * number_Of_Slices) - number_Of_Guests

print("Number of boxes of pizza to buy is: ",  number_Of_Boxes)
print("The remnant from the box of pizza: ",  remaining_Slice)
print("The price of the pizza is: ",  price)



