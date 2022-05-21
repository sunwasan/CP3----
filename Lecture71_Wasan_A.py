#กรอกชื่อสินค้า
#กรอกราคา
#วนจนถึง
#พิมพ์Exitเพื่อออก
menuList = []
priceList =[]
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.capitalize() == "Exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
def showReceipt():
    print("=======Receipt=======")
    for i in range(len(menuList)):
     print(menuList[i],priceList[i],"THB")
    print("Total :",sum(priceList),"THB")
    print("Thank you !")
showReceipt()



