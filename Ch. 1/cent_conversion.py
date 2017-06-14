input_cents = int(input("enter an amount of cents"))

quarters = input_cents // 25
dimes = (input_cents % 25) // 10
nickles = ((input_cents % 25) % 10) // 5
pennies = input_cents % 5

print(quarters,"quarters,",dimes,"dimes,",nickles,"nickles,",pennies,"pennies")
