secret_num = 6
guess = 0
found = False

while guess < 5:
    user_guess = int(input("Guess a number: "))
    guess += 1

    if user_guess == secret_num:
        found = True
        print("Congratulations, you found the secret number")
        break
    elif user_guess < secret_num:
        print("Too low")
    else:
        print("Too high")

if not found:
    print("Ohh NOOO!!! You can't find it.")
    


