# Write your solution here
"""
1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: Today I ate porridge
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
1 - add an entry, 2 - read entries, 0 - quit
Function: 1
Diary entry: I went to the sauna in the evening
Diary saved

1 - add an entry, 2 - read entries, 0 - quit
Function: 2
Entries:
Today I ate porridge
I went to the sauna in the evening
1 - add an entry, 2 - read entries, 0 - quit
Function: 0
Bye now!
"""

# read entries
def read_entries(filename:str):
    entries = ""
    with open(filename) as journal:
        for sentence in journal:
            entries += sentence
    return entries

def write_entries(filename:str, user_input:str):
  
    with open(filename,"w") as journal:
        journal.write(user_input)

def entry_journal(filename:str, journal:str):
    print("Diary entry: ")
    diary_entry = input()
    journal += diary_entry + "\n"
    write_entries(filename, journal)
    print("Diary saved")
    return journal

def read_journal(filename:str):
    print("Entries: ")
    journal = read_entries(filename)
    print(journal)
def main():
    import math
    filename = "diary.txt"
    journal = read_entries(filename)
    command = 2
    while command > 0:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        command = int(input("Function: "))

        if command == 1:
            # add entry and update the main one
            journal=entry_journal(filename, journal)

        elif command == 2:
            read_journal(filename)


    print("Bye now!")

main()