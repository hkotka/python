class ShortInputException(Exception):
    '''User defined exception class'''
    def __init__(self, lenght, atleast):
        Exception.__init__(self)
        self.lenght = lenght
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Why did you do an EOF?')
except ShortInputException as ex:
    print('ShortInputException: The input was {0} long, expected at least {1}'\
    .format(ex.lenght, ex.atleast))
else:
    print('No exception was raised.')