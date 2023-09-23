# Write your solution here
def same_chars(a_string, pos_1, pos_2):
    string_len = len(a_string)

    if string_len > pos_1 and pos_2 < string_len:
        return a_string[pos_1] == a_string[pos_2]
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))