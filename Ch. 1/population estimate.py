import math
CURRENT_POPULATION = 307357870

elapsed_yrs = int(input("Enter the amount of years for estimated population growth"))

births = math.ceil(elapsed_yrs * 4505142.857)
deaths = math.ceil(elapsed_yrs * 2425846.154)
imigrants = math.ceil(elapsed_yrs * 901028.571429)

population_est = CURRENT_POPULATION + births - deaths + imigrants

print("The estimated population in", elapsed_yrs, "years is", population_est)
