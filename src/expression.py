from stack import Stack

operatorIndex = {'+': 0, '-': 1, '*': 2, '/': 3, '(': 4, ')': 5, '#': 6}

operatorPriority = [[">", ">", "<", "<", "<", ">", ">"],
                    [">", ">", "<", "<", "<", ">", ">"],
                    [">", ">", ">", ">", "<", ">", ">"],
                    [">", ">", ">", ">", "<", ">", ">"],
                    ["<", "<", "<", "<", "<", "=", "NA"],
                    [">", ">", ">", ">", "NA", ">", ">"],
                    ["<", "<", "<", "<", "<", "NA", "="]]

def compareOperators(t1, t2):
    if (not t1 in operatorIndex) or (not t2 in operatorIndex):
        print(t1, t2, "Error: invalid operator to compare!")
        return "NA"
    else:
        return operatorPriority[operatorIndex[t1]][operatorIndex[t2]]

def parseInput(input):
    input = input.strip("\n")
    input = input.replace(" ", "")
    chars = list(input)
    items = []

    numberStr = ""

    for char in chars:
        if char.isdigit():
            numberStr += char
        else:
            if (numberStr != ""):
                items.append(numberStr)
            items.append(char)
            numberStr = ""

    items.append(numberStr)
    items.append("#")

    return items


def calculate(a, t, b):
    #print("calculate", a, t, b)
    if t == '+':
        return str(int(int(a) + int(b)))
    elif t == '-':
        return str(int(int(a) - int(b)))
    elif t == '*':
        return str(int(int(a) * int(b)))
    elif t == '/':
        return str(int(int(a)/ int(b)))
    else:
        print(t, "Error: invalid operator in your expression!")
        return None



def process_expression(items):
    stack_OPND = Stack()
    stack_OPTR = Stack()

    stack_OPTR.push("#")

    index = 0
    w = items[index]
    while w != "#" or stack_OPTR.get_top() != "#":
        if w.isdigit():
            stack_OPND.push(w)
            index += 1
        else:

            cr = compareOperators(stack_OPTR.get_top(), w)
            if cr == "=":
                stack_OPTR.pop()
                index += 1
            elif cr == '<':
                stack_OPTR.push(w)
                index += 1
            elif cr == '>':
                t = stack_OPTR.pop()
                b = stack_OPND.pop()
                a = stack_OPND.pop()

                c = calculate(a, t, b)

                stack_OPND.push(c)
            else:
                print("Error!")
                break


        w = items[index]

    return stack_OPND.pop()


if __name__ == "__main__":
    #print("Input your expression:")

    #expression = "7 + 12"  #19
    #expression = "4 * 3 + 2 / 2 " #13
    expression = "2 * 3 /(4 - 1) + 5 - 6" # 1

    #expression = sys.stdin.readline().strip('\n')


    items = parseInput(expression)

    print(expression, "->", items)

    result = process_expression(items)

    print(result)

