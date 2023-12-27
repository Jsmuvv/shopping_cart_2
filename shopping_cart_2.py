clothings = {}

prices = []

total = 0

while True:
    
    option = input("Do you want to add or delete the item?")
    if option == "add" :
        
        

    
        clothing = input("Enter clothes option to buy (x to quit): ")
        if clothing == "x":
            break
        price = float(input(f'Enter the price of a {clothing}: $'))
        clothings[clothing] = price
        prices.append(price)
    elif option == "delete":
        print(clothings)
        item = input("What item do you want to delete?")
        del clothings[item]

print("---YOUR CART---")

for cloth in clothings:
    print(cloth)

for price in clothings.values():
    total += price

print()
print(f"your total is: ${total}")