order1 = "pizza"
order1Quantity = 1
order1Price = 20

order2 = "cofe"
order2Quantity = 2
order2Price = 5

order3 = "water"
order3Quantity = 2
order3Price = 2

order1Cost = order1Quantity * order1Price
order2Cost = order2Quantity * order2Price
order3Cost = order3Quantity * order3Price

total = order1Cost + order3Cost + order3Cost
tax = total * 0.15
totalCost = total + tax

#final bill
print("Procodeing Restaurant")
print(f"1-{order1} = {order1Quantity} X {order1Price} = {order1Cost}$")
print(f"2-{order2} = {order2Quantity} X {order2Price} = {order2Cost}$")
print(f"3-{order3} = {order3Quantity} X {order3Price} = {order3Cost}$")

print("---------------")
print(f"Total = {total}$")
print(f"Tax = {tax}$")
print("---------------")

print(f"Total Cost = {totalCost}$")
print("Tank you")
