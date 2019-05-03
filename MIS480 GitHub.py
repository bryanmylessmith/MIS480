
class Automobile:
 
    def __init__(self):
        self.make = ' '
        self.model = ' '
        self.color = ' '
        self.year = 0
        self.mileage = 0
 
    def add_vehicle(self):
        self.make = input('Enter Make: ')
        self.model = input('Enter Model: ')
        self.color = input('Enter Color: ')
        self.year = int(input('Enter Year: '))
        self.mileage = int(input('Enter Mileage: '))
 
    def __str__(self):
        return('Make: %s Model: %s Color: %s Year: %d Mileage: %d' %
              (self.make, self.model, self. color, self.year,
               self.mileage))
 
vehicle_list = []
 
def update(vehicle_list):
    pos = int(input('Enter the Vehicle Number to Update: '))
    new_vehicle = car.add_vehicle(), car.__str__()
    vehicle_list[pos-1] = new_vehicle
    print('Vehicle has been updated')
 
while True:
    print ('''
    1.Add a New Vehicle
    2.Remove a Vehicle
    3.Update Vehicle Attributes
    4.View Vehicle Inventory
    ''')
 
    entry=input('Choose an Option: ') 
    if entry == "1": 
        print ('Add New Vehicle')
        car = Automobile()
        car.add_vehicle()
        vehicle_list.append(car.__str__())
    elif entry == "2":
        for i in vehicle_list:
            vehicle_list.pop(int(input('Enter the Vehicle Number to Remove: ')))
            print('Vehicle removed')
    elif entry == "3":
        print ('Update Vehicle')
        update(vehicle_list)
    elif entry == "4":
        print('List of Vehicles')
        print(vehicle_list)    
    else:
        print('Choose Another Option')
