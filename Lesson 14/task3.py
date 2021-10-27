
def arg_rules(type_: type, max_lenght: int, contains: list):
    def wrap(func):
        def check_string(*args: str):
            errors = []
            if type("".join(args)) != type_:
                errors.append(
                    f"\n— Your data does not match the specified type {type_}"
                )
            if len("".join(args)) > max_lenght:
                errors.append(
                    f"\n— Text length is more than {max_lenght} characters"
                )
            for i in contains:
                if "".join(args).find(i) == -1:
                    errors.append(f'\n— Not found "{i}"')
            if len(errors) > 0:
                print(f'Your mistakes: {", ".join(errors)}')
                return False
            else:
                return func("".join(args))

        return check_string

    return wrap

@arg_rules(str, 15, ["com", "@"])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("kholod@to.com"))
