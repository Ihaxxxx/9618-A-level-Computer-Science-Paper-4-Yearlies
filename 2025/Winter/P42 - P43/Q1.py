class Bird:
    #  DECLARE PRIVATE DistancePerHour : REAL
    #  DECLARE PRIVATE XPosition : REAL
    #  DECLARE PRIVATE YPosition : REAL
    #  DECLARE PRIVATE Species : STRING

    def __init__(self, pDistancePerHour, pSpecies):
        self.__Species = pSpecies 
        self.__DistancePerHour = pDistancePerHour 
        self.__XPosition = 500.0 
        self.__YPosition = 500.0 

    def GetPosition(self):
        ReturnValue = f"X = {self.__XPosition} Y = {self.__YPosition}"
        return ReturnValue

    def GetSpecies(self):
        return self.__Species

    def Move(self,direction,minutes):
        print(minutes)
        if Direction == "E":
            self.__XPosition = self.__XPosition + ((self.__DistancePerHour/60)*minutes)

        elif Direction == "W":
            self.__XPosition = self.__XPosition - ((self.__DistancePerHour/60)*minutes)

        elif Direction == "N":
            self.__YPosition = self.__YPosition + ((self.__DistancePerHour/60)*minutes)

        elif Direction == "S":
            self.__YPosition = self.__YPosition - ((self.__DistancePerHour/60)*minutes)
    
Bird1 = Bird(71.0, "Cockatiel")
Bird2 = Bird(56.0, "Macaw")

Bird1.GetPosition()
Bird2.GetPosition()

Choice = 0
while Choice != 1 and Choice != 2:
    print("Enter 1 for", Bird1.GetSpecies(), "is currently at", Bird1.GetPosition())
    Choice = -1

    print("Enter 2 for", Bird2.GetSpecies(), "is currently at", Bird2.GetPosition())

    Choice = int(input("Which bird do you want to move : "))


Time = -1
while Time < 0 or Time > 500:
    Time = int(input("To the nearest minute how long has the bird been flying : "))

Valid = False
while Valid == False:
    Valid = True
    Direction = input("Which direction has the bird been flying, North, South, East or West : ").upper()

    if Direction == "NORTH" or Direction == "N":
        if Choice == 1:
            Bird1.Move("N", Time)
        else:
            Bird2.Move("N", Time)

    elif Direction == "SOUTH" or Direction == "S":
        if Choice == 1:
            Bird1.Move("S", Time)
        else:
            Bird2.Move("S", Time)

    elif Direction == "EAST" or Direction == "E":
        if Choice == 1:
            Bird1.Move("E", Time)
        else:
            Bird2.Move("E", Time)

    elif Direction == "WEST" or Direction == "W":
        if Choice == 1:
            Bird1.Move("W", Time)
        else:
            Bird2.Move("W", Time)

    else:
        Valid = False

print(Bird1.GetSpecies(), "is currently at", Bird1.GetPosition())
print(Bird2.GetSpecies(), "is currently at", Bird2.GetPosition())