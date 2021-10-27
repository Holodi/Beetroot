
def function_outside(pow):
    def function_inside(pow2):
        return [(i, i ** pow) for i in range(1, pow ** pow2, pow2 * 2)]

    return function_inside


print(function_outside(4)(1))
