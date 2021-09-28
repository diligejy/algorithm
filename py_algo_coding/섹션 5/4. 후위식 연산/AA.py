pro = input()
stack = []
for p in pro:
    if p.isdecimal():
        stack.append(int(p))
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if p == "+":
            stack.append(num2 + num1)
        elif p == "-":
            stack.append(num2 - num1)
        elif p == "*":
            stack.append(num2 * num1)
        elif p == "/":
            stack.append(num2 / num1)

print(stack[0])
