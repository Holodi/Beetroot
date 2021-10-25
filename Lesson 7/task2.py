# Creating a dictionary

def make_country(name="", capital=""):
    print("Створіть свою країну!")
    countries = dict()
    i = 1
    while True:
        name = input("Введіть назву країни: ")
        if len(name) != 0:
            capital = input("Назвіть столицю цієї країни: ")
            countries.update({f"Country №{i}": {"Name": name, "Capital": capital}})
            i += 1
        else:
            print(f"All created countries:\n{countries}")
            return False


make_country()