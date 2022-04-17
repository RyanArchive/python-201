def order_ice_scramble(name, **toppings):
    price = 50.00

    print(f"Name: {name}")
    print("Toppings:")

    for key, value in toppings.items():
        if value:
            price += 5.00
            print(f"\t{key}")
    
    return price

total_price = order_ice_scramble(
    "Ryan", 
    choco_syrup=True, 
    mini_marshamllows=True, 
    candy_sprinkles=False, 
    rice_crispies=False
)
print(f"Total: P {total_price}")