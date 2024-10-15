import math

Total_number_of_people = int(input())
total_number_of_buses = int(input())
Number_of_seats_for_bus = int(input())
adjust_factor = math.ceil(Total_number_of_people/Number_of_seats_for_bus)

if (adjust_factor>total_number_of_buses):
    print(adjust_factor-total_number_of_buses)
else:
    print("sufficient buses.")