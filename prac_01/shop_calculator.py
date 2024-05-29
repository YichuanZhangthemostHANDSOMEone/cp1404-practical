DISCOUNT_RATE = 0.9
DISCOUNT_PRICE = 100
item_number = int(input("Number of items:"))
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("Number of items:"))
price_list = []
for i in range(item_number):
    price = float(input("Price of item:"))
    while price < 0:
        print("Invalid price!")
        price = float(input("Price of item:"))
    price_list.append(price)
total_price = sum(price_list)
if total_price >= DISCOUNT_PRICE:
    total_price *= DISCOUNT_RATE
print(f"Total price for {item_number} items is ${total_price:.2f}")
