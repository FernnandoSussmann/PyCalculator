lambs = [lambda x,y: x + y,lambda x,y: x - y,lambda x,y: x * y,lambda x,y: x / y,lambda x,y: x ** y,lambda x,y: x ** (1/y)]
opt = int(raw_input("Select an option: 0 = +, 1 = -, 2 = *, 3 = /, 4 = **, 5 = root:"))
num = float(raw_input("First number:"))
num2 = float(raw_input("Second number:"))
print lambs[opt](num,num2)
