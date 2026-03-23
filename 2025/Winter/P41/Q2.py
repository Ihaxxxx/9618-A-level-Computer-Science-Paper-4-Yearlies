class Train :
    # DECLARE PRIVATE TrainIDNumber : STRING
    # DECLARE PRIVATE Route : Integer
    def __init__(self, pNumber, pRoute):
        self.__TrainIDNumber = pNumber 
        self.__Route = pRoute 

    def GetTrainIDNumber(self):
        return self.__TrainIDNumber

    def GetRoute(self):
        return self.__Route

class Station :
    # DECLARE PRIVATE NumberPlatforms : Integer
    # DECLARE PRIVATE NumberTrains : Integer
    # DECLARE PRIVATE StationID : STRING
    # DECLARE Trains ARRAY [0:9] OF Train
    def __init__(self, pID, pNumberOfPlatforms):
        self.__StationID = pID
        self.__NumberPlatforms = pNumberOfPlatforms
        self.__Trains = []
        self.__NumberTrains = 0
    
    def AddTrains(self,pTrain):
        if self.__NumberTrains >= self.__NumberPlatforms:
            return False
        else:
            self.__Trains.append(pTrain)
            self.__NumberTrains += 1
            return True
    
    def GetTrains(self):
        if self.__NumberTrains == 0:
            return "There are no trains"

        OutputLine = f"The trains at station {self.__StationID} are:\n"

        for x in range(self.__NumberTrains):
            OutputLine += f"{self.__Trains[x].GetTrainIDNumber()} on route number {self.__Trains[x].GetRoute()}\n"

        return OutputLine



FirstTrain = Train("12ADV",134)
SecondTrain = Train("33ART",20)
ThirdTrain = Train("9FKF",3)
FourthTrain = Train("21VBC",24)

Station1 = Station("STH",2)
Station2 = Station("NTH",1)

returnVal = Station1.AddTrains(FirstTrain)
if returnVal == False:
    print('Station is full')

returnVal = Station1.AddTrains(SecondTrain)
if returnVal == False:
    print('Station is full')

returnVal = Station1.AddTrains(ThirdTrain)
if returnVal == False:
    print('Station is full')

returnVal = Station2.AddTrains(FourthTrain)
if returnVal == False:
    print('Station is full')

print(Station1.GetTrains())
print(Station2.GetTrains())