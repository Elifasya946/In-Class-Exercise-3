n=int(input("Write a number: "))
result=1
current=1
while current<=n:
    result*=current
    current+=1
print(f"The factorial of {n} is {result}")

