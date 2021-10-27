
def stop_words(words: list):
    def wrap(func):
        def string_edited(*args, **kwargs):
            result = func(*args, **kwargs)
            for i in words:
                result = result.replace(i, "*")
            return result

        return string_edited

    return wrap


@stop_words(["pepsi", "BMW"])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Ihor"))
