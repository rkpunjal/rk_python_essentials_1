
print("WELCOME TO OUR USELESS STORE!")
print("*"*30)

item_name = input("What item are you purchasing? ")
item_price = float(input(f"What is the price of {item_name}? "))
item_quantity = int(input(f"How many {item_name} are you buying? "))
print(f"\nAdded {item_quantity} {item_name}(s) to shopping cart!")
print(f"Subtotal: ${item_price * item_quantity}")
