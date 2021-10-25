# A simple calculator

def make_operation(operand, *args):
    try:
        i = 0
        res_text = ""
        while i < len(args):
            if i < len(args) - 1 and str(abs(i)).isnumeric():
                res_text = res_text + str(args[i]) + operand
            elif i == len(args) - 1 and str(abs(i)).isnumeric():
                res_text = res_text + str(args[i])
            i += 1
        print(eval(res_text))
    except:
        print("Не правильно введені дані!")


make_operation("+", 7, 7, 2)
make_operation("-", 5, 5, -10, -20)
make_operation("*", 7, 6)