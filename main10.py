class Vehicle:
    def __init__(self,):
        self.make = None            
        self.model = None
        self.year = None
        self.weight = None

    def setMake(self,make:str):
        return make
    
    def setModel(self,model:str):
        return model

    def setYear(self,year:int):
        return year

    def setWeight(self,weight:float):
        return weight


    def NeedsMaintenance(self):
        return False

    def TripsSinceMaintenance(self):
        self.trips = int(0)



class Cars(Vehicle):
       def __init__(self):
          
          Vehicle.__init__(self)

       def Drive(self):
           isDriving = True and Vehicle.trips + 1
           if Vehicle.TripsSinceMaintenance > 100:
                   Vehicle.NeedsMaintenance = True

       def Stop(self):
           isDriving = False and Vehicle.trips + 1
           if Vehicle.TripsSinceMaintenance > 100:
                   Vehicle.NeedsMaintenance = True
       
       def Repair(self):
           Vehicle.TripsSinceMaintenance = 0
           Vehicle.NeedsMaintenance = False

       def Reset(self):
           if trips > 100:
              Vehicle.NeedsMaintenance = False


def main():
    coche1 = Cars()
    coche1.setMake = "Ford"
    coche1.setModel = "KUGA"
    coche1.setYear = 2010
    coche1.setWeight = 1550.50
    coche1.TripsSinceMaintenance = 99
    coche1.NeedsMaintenance = False

    

    coche2 = Cars()
    coche2.setMake = "Ford"
    coche2.setModel = "Fiesta"
    coche2.setYear = 2015
    coche2.setWeight = 1050.75
    coche2.TripsSinceMaintenance = 55
    coche2.NeedsMaintenance = False

    coche3 = Cars()
    coche3.setMake = "Mercedes"
    coche3.setModel = "GLC 350"
    coche3.setYear = 2019
    coche3.setWeight = 1995.50
    coche3.TripsSinceMaintenance = 110
    coche3.NeedsMaintenance = True

    print(coche1.setMake,coche1.setModel,coche1.setYear,coche1.setWeight,coche1.NeedsMaintenance,coche1.TripsSinceMaintenance)

    print(coche2.setMake,coche2.setModel,coche2.setYear,coche2.setWeight,coche2.NeedsMaintenance,coche2.TripsSinceMaintenance)

    print(coche3.setMake,coche3.setModel,coche3.setYear,coche3.setWeight,coche3.NeedsMaintenance,coche3.TripsSinceMaintenance)


main()

    

    


           