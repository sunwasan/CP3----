def login():
    usernameIn = input("Username:")
    passwordIn = input("Password:")
    if usernameIn == "admin" and passwordIn == "1234":
        return showMenu()
    else:
        return False
def showMenu():
    print("1.Vat Calculator")
    print("2.Price Calculator")
    return  menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculate()
    elif userSelected ==2 :
        return priceCalculate()
def vatCalculate():
    price1 = int(input("First Product:"))
    price2 = int(input("Seccond Product:"))
    totalPrice = price1+price2
    return totalPrice+((totalPrice*7)/100)
def priceCalculate():
    price1 = int(input("First Product:"))
    price2 = int(input("Seccond Product:"))
    totalPrice = price1 + price2
    return totalPrice
print(login())