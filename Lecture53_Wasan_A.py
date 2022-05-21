def vatCalculate(totalPrice):
    result = (totalPrice*7/100)+totalPrice
    return result

price = int(input("ราคา :"))
print(int(vatCalculate(price)))


