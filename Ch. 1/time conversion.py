number = int(input("give a number of seconds"))

seconds = number % 60
minuets = (number // 60) % 60
hours = (number // 3600) % 24
days = (number // 86400) % 365
years = number // 31536000

print(years,"years,",days,"days,",hours,"hours,",minuets,"minuets,",seconds,"seconds")
