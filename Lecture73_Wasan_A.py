menuList = []
menuChoice = {'a':'120','b':'100','c':'50'}
while True:
     menuName = input("Please Enter Menu :")
     if(menuName.capitalize() == "Exit"):
        break
     menuList.append([menuName,menuChoice[menuName]])
def showReceipt():
    total = 0
    print("=======Receipt=======")
    for i in range(len(menuList)):
        print(menuList[i][0],'ราคา :',menuList[i][1],'บาท')
        total +=int(menuList[i][1])
    print('ราคารวมทั้งหมด :',total,'บาท')
showReceipt()

