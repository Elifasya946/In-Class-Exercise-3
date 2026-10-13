given_number=int(input("Write a number: "))
negative= given_number<0
abs_val= abs(given_number)
guess_number=0
while guess_number**3<abs_val:
    guess_number+=1

if guess_number**3==abs_val:

    if negative:
        guess_number=-guess_number
    print(f"The cube root of {given_number} is {guess_number}")
else:
    print(f"{given_number} is not a perfect cube!")

    


