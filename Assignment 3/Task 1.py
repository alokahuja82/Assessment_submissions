a = int(input("Enter a number: "))

def fact(a):
    if a<2:
        return 1
    else:
        return a * fact(a-1)

ans = fact(a)
print("The factorial of" ,a ,"is:",ans)
