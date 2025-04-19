
secret_number = 9
guess_count = 0
guess_limit = 3
print('Welcome to my game!')
print('You have 3 guesses to find the secret number')
print('Guess a number between 0 and 10')
while guess_count < guess_limit:
    guess_count += 1
    guess = input(f'Guess {guess_count}: ')
    guess = int(guess)
    if guess == secret_number:
        print('You won!')
        break
    elif guess < secret_number:
        print('Too low')
    else:
        print('Too high')
else:
    print('You lost!')

