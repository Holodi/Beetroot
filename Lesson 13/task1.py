
def number_of_locals(func):
    return func.__code__.co_nlocals

def test_function():
    a = 1
    b = 2.5
    c = "string"

print(number_of_locals(test_function))
