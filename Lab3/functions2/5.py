from dictionaries import movies

def average_score_by_category(category_name):
    totalScores = 0
    countOfMovies = 0

    for movie in movies:
        if movie['category'].lower() == category_name.lower():  # Учитываем регистр
            totalScores += movie['imdb']
            countOfMovies += 1

    if countOfMovies == 0:
        return f"No movies found in the category '{category_name}'."

    return totalScores / countOfMovies

# Ввод категории 
print(average_score_by_category(input("Enter category: ")))
