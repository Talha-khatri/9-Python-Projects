low = 1
high = 100
feedback = ''

print("Think of a number between 1 and 100 and I'll try to guess it!")

while True:
    if low > high:
        print("Hmm, something doesn't add up. Are you giving the right hints?")
        break
    guess = (low + high) // 2
    print("Is", guess, "too high (H), too low (L), or correct (C)?")
    feedback = input().lower()
    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'c':
        print("Yay! I guessed your number,", guess)
        break
    else:
        print("Please enter H, L, or C.")
