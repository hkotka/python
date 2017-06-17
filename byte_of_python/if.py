number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratulations, you guessed it!')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, its a little higher than that')
else:
    print('No, its a little lower than that')

print('Done')