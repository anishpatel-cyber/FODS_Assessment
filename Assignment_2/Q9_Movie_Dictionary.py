#Program that ask details of 3 movies and displays output in well formatted manner.

movies = {}

for i in range(3):
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    year = input("Enter year: ")
    rating = input("Enter rating: ")

    movies[title] = {
        "Director": director,
        "Year": year,
        "Rating": rating
    }

print("\nMovie Details:")
for title, info in movies.items():
    print(title, "-", info)