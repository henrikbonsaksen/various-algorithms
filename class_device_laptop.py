# Assignment 6 hbo050 #
# 1.
#
# a) A B D G H E I C F J


# 2. 

class Device:
    def __init__(self, __energy_level):
        self.__energy_level = __energy_level
    
    def get_energy(self):
        return self.__energy_level

    def __str__(self):
        return "This is dead device."


class Laptop(Device):
    def __init__(self, __energy_level):
        super().__init__(__energy_level)
        self.__battery = 0
    
    def get_battery(self):
        return self.__battery

    def get_energy(self):
        return self._Device__energy_level
        
    def charge(self):
        self.__battery = 100
        self._Device__energy_level = "A++"



my_laptop = Laptop("A+")
print(my_laptop)
print("Energy level:  ", my_laptop.get_energy())
print("Battery %: ", my_laptop.get_battery())
print("Charging...")
my_laptop.charge()
print("New energy level", my_laptop.get_energy())
print("New battery %: ", my_laptop.get_battery())
print("Wowee! Not dead anymore!")


# 3.
# litt usikker på denne oppgaven nøyaktig hva hensikten var, da i oppgaveteksten setter vi Guitar() 
# sin input til 6, og vi vil også ha ut outputen 6 strings. 
# Trodde poenget var at subklassen skulle overskrive?
# 

class MusicalInstrument:
    def __init__(self, num_of_strings):
        self.num_of_strings = num_of_strings
        print(self.num_of_strings) # printer ut original input

class Guitar(MusicalInstrument):
    def __init__(self, num_of_strings):
        super().__init__(num_of_strings)
        self.num_of_strings = 6

    def play(self):
        print("Guitar has", self.num_of_strings, "strings.")
    

class Violin(MusicalInstrument):
    def __init__(self, num_of_strings):
        super().__init__(num_of_strings)
        self.num_of_strings = 4

    def play(self):
        print("Violin has", self.num_of_strings, "strings.")


my_guitar = Guitar(10000000) # vil bli overskrevet av den bestemte num_of_strings i subklassen Guitar()
my_violin = Violin(99999999999999999) # samme her, bare for Violin()

my_guitar.play()
my_violin.play()