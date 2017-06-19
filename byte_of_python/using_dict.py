addressBook = {  'Swaroop'   :   'swaroop@swaroop.com',
        'Larry'     :   'larry@larry.se',
        'Simo'      :   'simo@simoland.fi',
        'Matsumoto' :   'matsumoto.mitsubishi@fuji.jp'
}

print("Swaroop's address is", addressBook['Swaroop'])

# Deleting a key-value pair
del addressBook['Simo']

print('\nThere are {0} contacts in the address-book\n'.format(len(addressBook)))

for name, address in addressBook.items():
    print('Contact {0} at {1}'.format(name, address))

# Adding a key-valye pair
addressBook['Guido'] = 'guido@python.org'

if 'Guido' in addressBook:
    print("\nGuido's address is", addressBook['Guido'])

# Dict does not contain Mikko
if addressBook.__contains__('Mikko'):
    print('Mikko is in the dict')
