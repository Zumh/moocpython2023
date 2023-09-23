# Write your solution here
def find_movies(database: list, search_term: str):
    collection_found = []

    for movie in database:
        if search_term.lower() in movie["name"].lower():
            collection_found.append(movie)
    
    return collection_found