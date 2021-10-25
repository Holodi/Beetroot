#The valid phone number program

def main():
    number = input('Введіть Ваш номер телефону: ')
    if number in(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) == False:
        print("Будь ласка введіть коректний номер телефону")
    elif len(number) == 10:
        print ("Дякуємо!")
    else:
        print("Ви ввели неправильний номер телефону.")
        main()

if  "main":
    main()
    input("Натисніть Enter щоб вийти ")
