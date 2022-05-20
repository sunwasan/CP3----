number = int(input("จำนวนดอกจันทร์:"))
blank = " "
for x in range (number):
    print(blank*(number-x),(2*x+1)*"*")

