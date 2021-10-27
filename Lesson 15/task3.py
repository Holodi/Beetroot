from functools import wraps

class TypeDecorator:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def converter(*args, **kwargs):
            for arg in args:
                if arg.isnumeric():
                    return int(arg)
                else:
                    return f"It's impossible"

        return converter

    @staticmethod
    def to_str(func):
        @wraps(func)
        def converter(*args, **kwargs):
            return str(' '.join(args))

        return converter

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def converter(*args, **kwargs):
            return bool(' '.join(args))

        return converter

    @staticmethod
    def to_float(func):
        @wraps(func)
        def converter(*args, **kwargs):
            for arg in args:
                try:
                    if arg.find(".") > 0:
                        integer, decimal = arg.split(".")
                    elif arg.find(",") > 0:
                        integer, decimal = arg.split(",")
                    else:
                        return f"It's impossible"
                    if integer.isnumeric() and decimal.isnumeric():
                        return float(int(integer) + \
                                     int(decimal) / (10 ** len(decimal)))
                    else:
                        return f"It's impossible"
                except Exception:
                    return f"It's impossible"
        return converter

@TypeDecorator.to_int
def do_nothing(string: str):
    return string

@TypeDecorator.to_str
def do_nothing2(string: str):
    return string

@TypeDecorator.to_bool
def do_something(string: str):
    return string

@TypeDecorator.to_float
def do_nothing3(string: str):
    return string

assert do_nothing("25") == 25
assert do_nothing2("Kholod Ihor") == "Kholod Ihor"
assert do_something("True") == True
assert do_nothing3("25,234") == 25.234
