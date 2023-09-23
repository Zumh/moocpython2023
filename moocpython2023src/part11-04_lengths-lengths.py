# WRITE YOUR SOLUTION HERE:

def lengths(given_lengths: list):
    return [len(current_list) for current_list in given_lengths]
if __name__ == "__main__":
    lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(lengths(lists))   