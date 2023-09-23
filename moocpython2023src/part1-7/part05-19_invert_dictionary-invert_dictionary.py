# Write your solution here
def invert(dictionary: dict):
    invert_dict = {}
    # copy dictionary to invert dict 
    for key, value in dictionary.items():
        invert_dict[value] = key 
    for key, value in invert_dict.items():
        del dictionary[value]
        dictionary[key] = value
