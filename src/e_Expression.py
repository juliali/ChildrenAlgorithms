from stack import Stack
from expression import parseInput, compareOperators


def process_expression(items):
    result = None # result is the calculation result of the expression

    stack_OPND = Stack()
    stack_OPTR = Stack()

    stack_OPTR.push("#")

    index = 0
    w = items[index]
    while w != "#" or stack_OPTR.get_top() != "#":
        ### TODO： Add logic here

        w = items[index]

    result = stack_OPND.pop()
    return result


if __name__ == "__main__":

    cr = compareOperators("+", "*")
    print("The compare result of + and * is:", cr)

    expression = "5 - 2"  #3
#    expression = "7 + 12"  #19
#    expression = "4 * 3 + 2 / 2 " #13
#    expression = "2 * 3 /(4 - 1) + 5 - 6" # 1

    items = parseInput(expression)
    print(expression, "->", items)

    result = process_expression(items)
    print(result)
