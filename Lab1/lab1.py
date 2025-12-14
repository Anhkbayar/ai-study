day_1 = ['wake up', 'lecture','sleep','breakfast', 'study', 'lecture','study', 'dinner','video games', 'sleep']
day_2 = ['wake up','breakfast', 'go to school','go home', 'lunch', 'study', 'dinner','sleep']
day_3 = ['wake up', 'breakfast', 'go to school', 'lunch', 'go to school','go home','dinner','study', 'sleep']
day_4 = ['wake up', 'breakfast', 'go to school', 'go home', 'lunch', 'study', 'dinner','video games', 'sleep']
day_5 = ['wake up', 'breakfast', 'go to school', 'go home','lunch', 'sleep','video games','dinner','video games', 'sleep']

all_days = [day_1, day_2, day_3, day_4, day_5]

all_locations = []
for day in all_days:
    all_locations.extend(day)

unique_locations = set(all_locations)

location_counts = {}
for location in unique_locations:
    location_counts[location] = all_locations.count(location)

sorted_locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)

print("Unique locations visited:")
for location, count in sorted_locations:
    print(f"{location}: {count} times")
  