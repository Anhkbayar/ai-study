day_1 = ['home', 'school','restaurant', 'home']
day_2 = ['home', 'school','restaurant', 'home']
day_3 = ['school', 'home']
day_4 = ['home', 'restaurant', 'home']
days = day_1 + day_2 + day_3 + day_4

unique_locations = set(days)

for locations in unique_locations:
    print(f"{locations}: {days.count(locations)}")