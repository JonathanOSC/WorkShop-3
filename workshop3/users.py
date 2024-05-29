""""
This class contains the information from the users.

Author: Jonathan Ochoa
"""

from vehicles.vehicles import Vehicle, Car, Truck, Motorcycle, Scooter, Helicopter, Yacht

class User:

    def __init__(self, username: str, password: str, user_type: str) -> None:
        self.username = username
        self.password = password
        self.user_type = user_type



class Admin(User):



    def create_vehicle(self, type_vehicle) -> Vehicle:
        
        """
        This method lets create a new vechicle and add it to the catalog

        Parameter:
        - type_vehicle (str): The type of the vechicle
        """

        chasis = input("Write the chassis of the vehicle (A or B): ")
        if chasis not in ["A", "B"]:
            raise ValueError("Error: Chassis wrote is wrong, Must be A or B.")

        model = input("Write the model of the vehicle: ")

        year = int(input("Writhe the year of the vehicle (Should be greater or equal than 2000): "))
        if year < 2000:
            raise ValueError("Error. Year is not in a valid range.")

        engine_name = input("Write the name of the motor for the vehicle: ")
        
        price = float(input("Write the price of the vehicle: "))
        consumption = float(input("Write the consumption for the vehicle: "))

        try:
            engine = engines[engine_name]

            if type_vehicle == "car":
                
                
                transmission = input("Write the transmission of the vehicle: ")
                trade = input("Write the trade for the vehicle: ")
                combustible_type = input("Write the combustible_type for the vehicle: ")
                
                vehicle_obj_new = Car(engine, chasis, price, model, year, consumption, transmission, trade, combustible_type)
            elif type_vehicle == "truck":
                vehicle_obj_new = Truck(engine, chasis, price, model, year, consumption)
            elif type_vehicle == "yatch":
                vehicle_obj_new = Yacht(engine, chasis, price, model, year, consumption)

                lenght = int(input("Write the lenght of the vehicle: "))
                weight = float(input("Write the weight of the vehicle: "))
                trade = input("Write the trade for the vehicle: ")

            elif type_vehicle == "motorcycle":
                vehicle_obj_new = Motorcycle(engine, chasis, price, model, year, consumption, lenght, weight, trade)

            elif type_vehicle == "helicopter":
                vehicle_obj_new = Helicopter(engine, chasis, price, model, year, consumption)
            elif type_vehicle == "scooter":
                vehicle_obj_new = Scooter(engine, chasis, price, model, year, consumption)


            vehicles.append(vehicle_obj_new)

        except Exception as e:
            print(f"Error: {e}.")

    def update_vehicle(self, vehicle: Vehicle) -> Vehicle:
        pass

    def delete_vehicle(self, vehicle: Vehicle) -> Vehicle:
        pass
    


class RegularUser(User):

    def search_vehicle(self, vehicle: Vehicle) -> Vehicle:
        pass