
def two_numbers():
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        return a ** 2 / b
    except (TypeError, ValueError):
        print("Це не числа!")
    except ZeroDivisionError:
        print("Ділення на нуль!")

print(two_numbers())