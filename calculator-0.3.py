x = float(input("enter a number : "))
y= float(input("enter another one : "))
op = input("enter an operation : ")
while op != "+" and op != "-" and op != "*" and op != "/" :
    op = input("please write corectly the operation : ")
match op :
    case "+" :
        print(x + y)
    case "-" :
        print(x - y)
    case "*" :
        print(x * y)
    case "/" :
        while y == 0 :
            y = int(input("Write the second number defrent from 0 :"))
        print(x / y)