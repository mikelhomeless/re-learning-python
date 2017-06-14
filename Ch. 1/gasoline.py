gallons = float(input("Enter an amount of gasoline in gallons: "))

liters = gallons * 3.78541
barrels = gallons / 19.5
co2_lbs = gallons * 20
gas_energy_btu = gallons * 115000
ethanol_equivalent_gal = gas_energy_btu / 75700
price_usd = 3.00 * gallons

print(gallons, "gallons of gas. . .")
print("Is Equivalent to", liters, "liters")
print(barrels, "barrels")
print("\nProduces", co2_lbs, "pounds of carbon")
print("Has the energy of", ethanol_equivalent_gal, "gallens of ethanol")
print("Costs", price_usd, "dollars")
