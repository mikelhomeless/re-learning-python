inches_str = input("How many inches of rain fell: ")
inches_float = float(inches_str)

volume = (inches_float / 12) * 43560
gallons = volume * 7.48051945

print(gallons, " gallons of rain fell on 1 acre of land.")
