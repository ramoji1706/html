 #2.take temperature from the user and convert foreign heat -> Celsius.
 # 3.take temperature from the user and convert Celsius → foreign heat.

temparature_in_farenheit = int(input("temparature_in_farenheit"))
temparature_in_degreecelsius = int(input("temparature_in_degreecelsius"))

farenheit_to_celcious = (temparature_in_farenheit -32)*5/9
celsius_to_farenheit = (temparature_in_degreecelsius*9/5) + 32

print(farenheit_to_celcious)
print(celsius_to_farenheit)