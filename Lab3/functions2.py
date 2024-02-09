from function_movies import movies

# task1
def score_5_5(movie_name):
    for m in movies:
        if m['name'] == movie_name:
            if m['imdb'] > 5.5:
                return True
    return False

print(score_5_5('Love'))

#task2
def sublist_5_5():
    score_above_5_5 = []
    for m in movies:
        if m['imdb'] > 5.5:
            score_above_5_5.append(m['name'])
    return score_above_5_5

print(sublist_5_5())

#task3
def category_list(category):
    category_movie = []
    for m in movies:
        if m['category'] == category:
            category_movie.append(m['name'])
    return category_movie

print(category_list('Romance'))

#task4
def computes_average():
    sum = 0
    count = len(movies)
    for m in movies:
        sum += m['imdb']
    return sum/count

print(round(computes_average(), 2))

#task5
def category_computes_average(category):
    sum_category_movie = 0
    for m in movies:
        if m['category'] == category:
            sum_category_movie += m['imdb']
    return sum_category_movie/len(category_list(category))

print(category_computes_average('Romance'))