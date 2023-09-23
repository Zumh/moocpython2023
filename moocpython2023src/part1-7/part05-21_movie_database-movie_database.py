# Write your solution here
def add_movie(database: list[dict], name: str, director: str, year: int, runtime: int):
    """
    name
    director
    year
    runtime
    """
    movie_info = {"name":name, "director":director,"year":year, "runtime":runtime}
    # check if the movie exist in the data if not add 
    database.append(movie_info)
    