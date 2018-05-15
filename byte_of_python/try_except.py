try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you EOF?')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('You entered {0}'.format(text))