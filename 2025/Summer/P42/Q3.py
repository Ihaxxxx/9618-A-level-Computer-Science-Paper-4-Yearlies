class Animal :
    # DECLARE PUBLIC Name : STRING
    # DECLARE PUBLIC Sound : STRING
    # DECLARE PUBLIC Size : INTEGER
    # DECLARE PUBLIC Intelligence : INTEGER
    def __init__(self, pName, pSound, pSize, pIntelligence):
        self.Name = pName 
        self.Sound = pSound
        self.Size = pSize 
        self.Intelligence = pIntelligence 

    def Description(self):
        Message = f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}"
        return Message

class Parrot(Animal) : 
    # DECLARE PUBLIC WingSpan : INTEGER
    # DECLARE PUBLIC NumberWords : INTEGER

    def __init__(self, pName, pSound, pSize, pIntelligence, pWingSpan, pNumberWords):
        super().__init__(pName, pSound, pSize, pIntelligence)
        self.WingSpan = pWingSpan
        self.NumberWords = pNumberWords

    def ChangeNumberWords(self, Change):
        self.NumberWords += Change

    def Description(self):
        Message = f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}. It has a wingspan of {self.WingSpan}cm and can say {self.NumberWords} words."
        return Message
    
class Wolf(Animal):
    # DECLARE PUBLIC TerritorySize : INTEGER
    def __init__(self, pName, pSound, pSize, pIntelligence, pTerritorySize):
        super().__init__(pName, pSound, pSize, pIntelligence)
        self.TerritorySize = pTerritorySize

    def SetTerritorySize(self, Change):
        self.TerritorySize += Change

    def Description(self):
        Message = f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}, it's territory is {self.TerritorySize} square miles."
        return Message

ParrotInstance = Parrot('Chewie','Squawk',1,10,30,29)
WolfInstance = Wolf('Nighteyes','Howl',8,7,100)
AnimalInstance = Animal('Copper','Neigh',10,6)

WolfInstance.SetTerritorySize(-20)
ParrotInstance.ChangeNumberWords(2)

print(ParrotInstance.Description())
print(WolfInstance.Description())
print(AnimalInstance.Description())

