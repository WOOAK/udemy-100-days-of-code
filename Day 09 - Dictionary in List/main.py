travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(Country,Visits,Cities):
    Travel_dictionary = {}
    Travel_dictionary["country"] = Country
    Travel_dictionary["visits"] = Visits
    Travel_dictionary["cities"] = Cities
    travel_log.append(Travel_dictionary)
    





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



