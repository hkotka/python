class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        print('I am constructed')
        self.name = z
    def __del__(self):
        print('I am destructed', self.x)
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count', self.x)

person = PartyAnimal('Timppa')

for i in range(10):
    person.party()

person = 42
print('animal contains', person)
