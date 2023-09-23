# Write your solution here
def get_recipie(file_name: str):
    recipie = []
    organize_recipie = []
    with open(file_name) as recipie_data:
        for each_recipie in recipie_data:
            each_recipie = each_recipie.strip()

            if each_recipie == "":
                organize_recipie.append(recipie)
                recipie = []
            else:
                recipie.append(each_recipie)
        organize_recipie.append(recipie)

    return organize_recipie

def search_by_name(filename: str, word: str):
    list_of_recipie = []
    # search the recipie
    organize_recipie = get_recipie(filename)

    for recipies in organize_recipie:

        if word in recipies[0].lower():
            list_of_recipie.append(recipies[0])

    return list_of_recipie

def search_by_time(filename: str, prep_time: int):
    recipie_name_time = []
    organize_recipie = get_recipie(filename)
    for recipes in organize_recipie:
        current_prep_time = int(recipes[1])
        if current_prep_time <= prep_time:
            recipie_name = recipes[0]
            current_prep_time = recipes[1]
            recipie_name_time.append(f"{recipie_name}, preparation time {current_prep_time} min")
    return recipie_name_time

def search_by_ingredient(filename: str, ingredient: str):
    recipie_name_time = []
    organize_recipie = get_recipie(filename)
    for recipes in organize_recipie:
        current_prep_time = int(recipes[1])
        if ingredient in recipes[2:]:
            recipie_name = recipes[0]
            current_prep_time = recipes[1]
            recipie_name_time.append(f"{recipie_name}, preparation time {current_prep_time} min")
    return recipie_name_time