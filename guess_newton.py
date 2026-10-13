x=int(input("What x to find the cube root of?: "))
guess=int(input("What guess to start with?: "))
current_cube=guess**3
print(f"Current cube: {current_cube}")
next_guess= guess-(guess**3-x)/(3*(guess**2))
print(f"Next guess: {next_guess}")



