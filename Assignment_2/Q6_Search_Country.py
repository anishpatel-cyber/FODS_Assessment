#Program that accepts list of countries and countries to be searched and 
#returns the index of the country if found.

def search_country(countries, target):
    if target in countries:
        return countries.index(target)
    else:
        return "Not Found in List"

countries = ["Nepal", "India", "China"]
print(search_country(countries, "China"))