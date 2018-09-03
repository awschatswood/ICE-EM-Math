x = int(input("please input how much mony you borrowed from bank: "))
y = float(input("the intereset rate is %, (e.g) 0.04: "))
z = int(input("How many years you need to pay the whole loan off: "))

total = x * (1.0+y)**z
totalincrease = (1.0+y)**z
totalint = total - x
simplerate = x * y * z 



print("")
print("Amount at the end of period is: %s:" % total)
print("Total compound interst paid is: %s" % totalint)
print("while simple reate is: %s" % simplerate)
