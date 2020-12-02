

#Creating a parent class of Eevee, the normal Pokemon!
#Which is ironic, as it's usually the child
class Eevee:
    legs = 4
    species = "Pokemon"
    pokemonType = "normal"
    favoriteAttack = "Tackle"

    def attack(self):
        msg = "Eevee is a {} Pokemon. They don't like to fight".format(self.pokemonType)
        return msg

#Creating a child class of Jolteon, one of Eevee's evolutions!
class Jolteon(Eevee):
    pokemonType = "Electric"
    favoriteAttack = "Thunderbolt"

    #I've engaged in polymorphism by changing Jolteon's attack method to differ from Eevee!
    def attack(self):
        msg = "Jolteon is a {} Pokemon. Its favorite attack is {}.".format(self.pokemonType, self.favoriteAttack)
        return msg

#Finally, a second child class of Vaporeon, another one of Eevee's evolutions.  
class Vaporeon(Eevee):
    pokemonType = "Water"
    favoriteAttack = "Water Gun"

    #Another sign of polymorphism, but I'm also adding a parameter for this method.
    def attack(self, favoriteToy):
        msg = "Vaporeon is a {} Pokemon. It doesn't like fighting other Pokemon, but it likes using {} on a {}.".format(self.pokemonType, self.favoriteAttack, favoriteToy)
        return msg


Butch = Eevee()
print(Butch.attack())

Jolty = Jolteon()
print(Jolty.attack())

Aqua = Vaporeon()
print(Aqua.attack("Beach Ball"))
