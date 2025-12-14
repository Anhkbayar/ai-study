day_1 = ['home', 'school','restaurant', 'home']
day_2 = ['home', 'school', 'home']
day_3 = ['school', 'home']
day_4 = ['home', 'restaurant', 'home']

all_days = [day_1, day_2, day_3, day_4]

# Collect all locations
all_locations = []
for day in all_days:
    all_locations.extend(day)

# Count visits
unique_locations = set(all_locations)

location_counts = {}
for location in unique_locations:
    location_counts[location] = all_locations.count(location)

# Sort by frequency (descending)
sorted_locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)

# Print results
print("Unique locations visited:")
for location, count in sorted_locations:
    print(f"{location}: visited {count} times")
