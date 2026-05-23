num1 = int(input("Выберите перове число: "))
num2 = int(input("Выберите второе число: "))
print ("Выберите действие: " 
               "1. Сложение",
               "2. Вычитание ")
chose = int(input( ))

if chose == 1:
    print(num1 + num2)
else:
    print(num1 - num2) 

