#HotelMenu

menu = {
    'Tea' : 50,
    'Coffee' : 60,
    'Sandwich' : 150,
    'Pizza' : 200,
    'Burger' : 120,
}

#greet the user
print("Welcome Python Hotel")
print("Please select from the menu below:")
#display the menu
for item, price in menu.items():
    print(f"{item}: {price} Rs")

total_bil = 0

#take order
order_1 = input("Please enter your order: ")
if order_1 in menu:
    total_bil += menu[order_1]
    print(f"Your order for {order_1} has been placed.")
else:
    print("Sorry, We don't have that item on the menu.")

#ask if user wants to order more
anotherOrder = input("Do you want to order more? (yes/no): ")

if anotherOrder == "yes":
    order_2 = input("Please enter your order: ")
    if order_2 in menu:
        total_bil += menu[order_2]
        print(f"Your order for {order_2} has been placed.")
        print(f"Your total bill is: {total_bil} Rs")
    else:
        print("Sorry, We don't have that item on the menu.")

else:
    print(f"Your total bill is: {total_bil} Rs")  
    print("Thank you for visiting Python Hotel!")

#ask if user wants to order more
anotherOrder = input("Do you want to order more? (yes/no): ")
if anotherOrder == "yes":
    order_3 = input("Please enter your order: ")
    if order_3 in menu:
        total_bil += menu[order_3]
        print(f"Your order for {order_3} has been placed.")
        print(f"Your total bill is: {total_bil} Rs")
    else:
        print("Sorry, We don't have that item on the menu.")     
else:
    print("Thank you for visiting Python Hotel!")

#ask if user wants to order more
anotherOrder = input("Do you want to order more? (yes/no): ")
if anotherOrder == "yes":
    order_4 = input("Please enter your order: ")
    if order_4 in menu:
        total_bil += menu[order_4]
        print(f"Your order for {order_4} has been placed.")
        print(f"Your total bill is: {total_bil} Rs")
    else:
        print("Sorry, We don't have that item on the menu.") 
else:
    print("Thank you for visiting Python Hotel!")
    
#ask if user wants to order more
anotherOrder = input("Do you want to order more? (yes/no): ")
if anotherOrder == "yes":
    order_5 = input("Please enter your order: ")
    if order_5 in menu:
        total_bil += menu[order_5]
        print(f"Your order for {order_5} has been placed.")
        print(f"Your total bill is: {total_bil} Rs")
    else:
        print("Sorry, We don't have that item on the menu.") 
else:
    print("Thank you for visiting Python Hotel!")