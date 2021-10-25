
def oops():

    raise KeyError("Помилка!")

def calls_oops(dictionary):
    try:
        print(dictionary["name"])
        oops()
    except:
        print("Помилка!")

sample_dict = dict(
    Name="Oleksii",
    Last_Name="Berezhnyi")

calls_oops(sample_dict)
