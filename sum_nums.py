n=int(input("Write a number: "))
sum=0
for i in range (1,n+1):
    sum+=i
print(f"The running sum is {sum}")
sum_gauss= n*(n+1)/2
print (f"The sum with using Gauss formula is {sum_gauss}")

if sum_gauss==sum:
    print("My running sum code works correctly")
else :
    print("My running sum code failed badly")
    