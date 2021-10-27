
def logger(func):
    def wraper(*args, **kwargs):
        print(f"{func.__name__} called with "
              f"{', '.join(str(arg) for arg in args)}")
    return wraper
  
@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(2, 3)
square_all(4, 5, 6, 7)
