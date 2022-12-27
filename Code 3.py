# comission calculator
# variable that needs to be created: sale price x comission % divide by 100

loop = "y"
loop2 = "y"

def ComissionCalc(price, percentage):
    print(float(price) * float(percentage) / 100)

while loop2 == "y":
    data1 = input("Enter product price: ")
    data2 = input("Enter comission percentage: ")
    ComissionCalc(data1, data2)
    loop = input("Calculate again? y/n: ")
    loop2 = loop.lower()


print("Have a nice day!")

