import catalog, factories.engines as engines, factories.factories as factories, vehicles.vehicles as vehicles


MESSAGE = """
Option 1. Create engine
Option 2. Create car
Option 3. Create truck
Option 4. Create yacht
Option 5. Create motorcycle
Option 6. Show engines
Option 7. Show vehicles
Option 8. Search by year
Option 9. Search by potency

Option 10. Exit"
"""


engines = {}
vehicles = []

def create_engine():
    """ This method lets add a new engine to list """

    name = input("Write engine name: ")
    type_engine = input("Write type of engine: ")
    potency = int(input("Write the potency of the engine: "))
    weight =  int(input("Write the weight of the engine: "))

    new_obj_engine = Engine(name, type_engine, potency, weight)
    engines[name] = new_obj_engine






def search_by_year(year: int) -> list:
    """
    This method makes a search of all vehicles of a specific year.

    Parameters:
    - year (int): Year to filter
    """

    return [v for v in vehicles if v.year == year]


def search_by_potency(potency: int):
    """
    This method makes a search of vehicles based on the potency of the engine of thje vehicle

    Parameters:
    - potency (int): Potency to be filtered
    """
    return [p for p in vehicles if p.engine.potency == potency]



print(MESSAGE)
option = int(input("Please, choise an option: "))

while option != 10:
    if option == 1:
        create_engine()
    elif option == 2:
        create_vehicle("car")
    elif option == 3:
        create_vehicle("truck")
    elif option == 4:
        create_vehicle("yacht")
    elif option == 5:
        create_vehicle("motorcycle")
    elif option == 6:
        for name, values in engines.items():
            print(f"{name} = {str(values)}")
    elif option == 7:
        for vehicle in vehicles:
            print(vehicle)
    elif option == 8:
        year = int(input("Please, write the year: "))
        search_by_year(year)
    elif option == 9:
        potency = int(input("Plkease, write the potency: "))
        search_by_potency(potency)
    else:
        print("Opción no válida")
    print("\n\n" + MESSAGE)
    option = int(input("Please, choice an option: "))


