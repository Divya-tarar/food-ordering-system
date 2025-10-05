print("Welcome to FoodZone")
print("Menu:")
print("1. Burger - ₹100")
print("2. Pizza - ₹200")
print("3. Fries - ₹80")
item = input("Enter the item you want to order: ")
if item == "Burger":
    total = 100
elif item == "Pizza":
    total = 200
elif item == "Fries":
    total = 80
else:
    print("Item not available.")
    total = 0
if total > 0:
    discount = input("Do you have a discount coupon? (yes/no): ")
    if discount == "yes":
        percent = int(input("Enter discount percentage: "))
        total = total - (total * percent / 100)
    print("Your total bill is ₹", total)
    confirm = input("Confirm order? (yes/no): ")
    if confirm == "yes":
        print ("Order placed successfully!")
    else:
        print ("Order cancelled.")
