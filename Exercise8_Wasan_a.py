usernameIn = input("Username:")
passwordIn = input("Password:")
if usernameIn=="admin" and passwordIn =="1234":
    print("Welcome",usernameIn,"!!!!")
    print("====Choose Your Product=======")
    print("1.LE Television","120","THB")
    print("2.Sumsing Television","300","THB")
    print("3.Sory Television","420","THB")
    userSelected = int(input("Choose No.:"))
    userQuantity = int(input("Quantity:"))
    if userSelected == 1:
        print("Total:",120*userQuantity,"THB")
    if userSelected == 2:
        print("Total:", 300 * userQuantity, "THB")
    elif userSelected == 3:
        print("Total:", 420 * userQuantity, "THB")
    print("Thank you for shopping!")
else:
    print("User not found")