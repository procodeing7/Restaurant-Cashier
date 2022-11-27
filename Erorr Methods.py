# Menu & Price & Counts
pizzaPrice = 20
pizzaCount = 1
pizza = pizzaCount * pizzaPrice

colaPrice = 5
colaCount = 2
cola = colaCount * colaPrice

waterPrice = 1.5 
waterBottle = 2
water = waterPrice * waterBottle

total = pizza + cola + water
tax = total * 0.15
totalCost = total + tax

# Print Area
print("Procodeing Restaurant")
print(f"1-Pizza = {pizzaCount} x {pizzaPrice} = {pizza}$")
print(f"2-Cola = {colaCount} x {colaPrice} = {cola}$")
print(f"3-Water = {waterBottle} x {waterPrice} = {water}$\n------------")

print(f"total = {total}$\ntax = {tax}$\n------------")
print(f"total Cost = {totalCost}$\nThank you")
