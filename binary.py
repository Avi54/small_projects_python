low = 1
high = 1000

print(f'num between {low} and {high}')
input('> ')

number_of_guesses = 1

while True:
    guess = low + (high - low) // 2
    high_low = input(f"{guess}. higher or lower, h or l ").casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("correct")
        break
    else:
        print("enter h, l or c ")

    number_of_guesses += 1
