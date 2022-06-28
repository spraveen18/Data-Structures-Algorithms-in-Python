
# Dictionary

locations = {'North America': {'USA': ['Mountain View']}}


locations['Asia'] = {'India': ['Bangalore']}
locations['North America']['USA'].append('Atlanta') 
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia']['China'] = ['Shanghai']

print(locations)

print(1)
sorted_usa = sorted(locations['North America']['USA'])
for city in sorted_usa:
    print("American", city)
    
    
print(2)
asian_cities = []
for countries, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countries
    asian_cities.append(city_country)
asia_sorted = sorted(asian_cities)
for city in asia_sorted:
    print("Asia", city)
