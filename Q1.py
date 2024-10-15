#Take the input from the user for(Total number of people,Number of seats for bus. Based on two inputs
#Decide how many number of buses required

import math

no_of_people = int(input("no_of_people"))
no_of_seats_for_bus = int(input("no_of_seats_for_bus"))

no_buses_required = math.ceil(no_of_people/no_of_seats_for_bus)

print(no_buses_required)

updated = 1