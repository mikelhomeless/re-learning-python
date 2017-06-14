VOYAGER_SPEED = 38241 #MPH assumes constant speed
#Voyager 1's distance from the sun as of 09/25/2009 in miles
VOYAGER1_START_DISTANCE = 16637000000

elapsed_days = int(input("Enter the number of days passed since 09/25/2009"))

distance_mi = VOYAGER1_START_DISTANCE + (VOYAGER_SPEED * 24 * elapsed_days)
distance_km = distance_mi * 1.609344
distance_au = distance_km / 149597870.700
light_hours_roundtrip = ((distance_km * 2) / 299792.458) / 3600

print("Distance in miles:",distance_mi)
print("Distance in kilometers:",distance_km)
print("Distance in Astronomical Units:",distance_au)
print("Time it would take for round-trip radio communication:",light_hours_roundtrip)
