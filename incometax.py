x = int(input("please input your annual income: "))

# between 12000- 30000
tax12=(30000 - 12000) * 0.15 

# between 30000- 75000
tax30=(75000 - 30000) * 0.25     


if x < 12000:
    print(" your tax is zero")
    
if x < 30000:
    tax = (x - 12000) * 0.15 
    print ("your tax is  ",  tax)
    
elif x < 75000:
    temp1 = (30000 - 12000) * 0.15 
    temp2 = (x-30000)* 0.25
    tax = temp1 + temp2
    print ("your tax is ",  tax)
    
elif x > 75000:
    temp1 = (30000 - 12000) * 0.15 
    temp2 = (75000-30000)* 0.25
    temp3 = (x-75000)* 0.35
    tax = temp1 + temp2 + temp3
    print ("your tax is  ",  tax)

