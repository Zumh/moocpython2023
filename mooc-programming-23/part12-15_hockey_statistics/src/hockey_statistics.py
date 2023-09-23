# Write your solution here

"""
search by name for a single player's stats
list all the abbreviations for team names in alphabetical order
list all the abbreviations for countries in alphabetical order
"""
import json 

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name 
        self.nationality = nationality
        self.assists = assists 
        self.goals = goals 
        self.penalties = penalties 
        self.team = team 
        self.games = games 

    def __str__(self) -> str:
        total_points = self.goals + self.assists
        return(f"{self.name:<21}{self.team:<5}{self.goals:>2} + {self.assists:>2} = {total_points:>3}")

class ManageFile:
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def load_file(self):
        """
        open file by a given file name return them as a list of string after we parse them
        """
        applicants = None
        with open(self.__file_name) as myfile:
            applicants = json.load(myfile)
        return applicants
    
 
class DataLogic:
    
    def __init__(self):
        self.__players = {}
    
    def add_players(self, input_player: dict):
        # transform dictionary to player object
        # then store with their unique name
        name = input_player['name']
        nationality = input_player['nationality']
        assists = input_player['assists']
        goals = input_player['goals']
        penalties = input_player['penalties']
        team = input_player['team']
        games = input_player['games']

        self.__players[name] = Player(name, nationality, assists, goals, penalties, team, games)

    def stats(self, current_player: Player):
        return current_player.goal + current_player.assists

    def search_by_name(self, search_name: str):
        """
        single player's stats
        """
        if search_name in self.__players:
            current_player = self.__players[search_name]
            return current_player
        return None

    def list_all_teams(self):
        """
        list all the abbreviations for team names in alphabetical order
        """
        team_names = []

        for name in self.__players:
            if self.__players[name].team not in team_names:
                team_names.append(self.__players[name].team)
        return sorted(team_names)
    

    def list_all_coutries(self):
        """
        list all the abbreviations for countries in alphabetical order
        """
        countries = []
        for name in self.__players:
            if self.__players[name].nationality not in countries:
                countries.append(self.__players[name].nationality)
        return sorted(countries)

    def search_by_team(self, team_name: str):

        # search player by the team name
        # sort player using point score from highest to lowest
        search_players = {player.goals + player.assists:player for name, player in self.__players.items() if player.team == team_name}
        return sorted(search_players.items(),reverse=True)
    
    def serach_by_nationality(self, country: str):

        # search player by the team name
        # sort player using point score from highest to lowest
        search_players = {player.goals + player.assists:player for name, player in self.__players.items() if player.nationality == country}
        return sorted(search_players.items(),reverse=True)
    def search_by_maxpoints(self, number_of_player: int):
        """
        list of n players who've scored the most points
        if two players have the same score, whoever has scored the higher number of goals comes first
        """
        # get a lit of sorted score from highest to lowest point
        organize_by_points = {(player.goals + player.assists, player.goals): player for name, player in self.__players.items()}
        return sorted(organize_by_points.items(), reverse=True)[:number_of_player]

    def search_by_maxgoals(self, number_of_player:int):
        """
        list of n players who've scored the most goals if two players have the same number of goals, 
        whoever has played the lower number of games comes first
        """
        # get a lit of sorted score from highest to lowest point
    
        return sorted(self.__players.items(), key=lambda player: (player[1].goals, -player[1].games), reverse=True)[:number_of_player]
   

class PlayerApplication:
    """
    This is an interface for dealing the entrance of data and also for output format.
    Also for a play ground for other classes to interact.
    """
    def __init__(self) -> None:

        file_name = input("file name: ")
        #file_name = "partial.json"
        # ManageFile will return dictionar of players info
        players = ManageFile(file_name).load_file()

        # applicants variable will parse and allow dtalogic to transform data into player object then store them in dictionary
        self.__applicants = DataLogic()
        for player in players:
            self.__applicants.add_players(player)

        print(f"read the data of {len(players)} players")

    def help(self):
        print(f"commands: \n\
        0 quit\n\
        1 search for player\n\
        2 teams \n\
        3 countries \n\
        4 players in team \n\
        5 players from country \n\
        6 most points \n\
        7 most goals")
    
    def search(self):
        search_name = input("name: ")
        player = self.__applicants.search_by_name(search_name)
        print(player)
    
    def teams(self):
        """
        List all team abreviation
        """
        for team_name in self.__applicants.list_all_teams():
            print(team_name)

    def countries(self):
        for country in self.__applicants.list_all_coutries():
            print(country)
    def players_in_team(self):
        team_name = input("team: ")
        for player in self.__applicants.search_by_team(team_name):
            print(player[1])
        

    def players_from_country(self):
        
        country_name = input("country: ")
        for player in self.__applicants.serach_by_nationality(country_name):
            print(player[1])

    def most_points(self):
        """
        list of n players who've scored the most points
        if two players have the same score, whoever has scored the higher number of goals comes first
        """
        number_of_player = int(input("how many: "))
        for player in self.__applicants.search_by_maxpoints(number_of_player):
            print(player[1])

    def goals(self):
        """
        list of n players who've scored the most goals if two players have the same number of goals, 
        whoever has played the lower number of games comes first
        """
        number_of_player = int(input("how many: "))
        for player in self.__applicants.search_by_maxgoals(number_of_player):
            print(player[1])
    def execute(self):
        # call file handling function here 

        # call help command 
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search()
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.goals()
            else:
                self.help()




NHL_player = PlayerApplication() 
NHL_player.execute()  

'''
import json
 
class Statistics:
    def __init__(self, players: list):
        self.__players = players
 
    def by_points(self,  p):
        return  p['goals'] + p['assists']
 
    def by_goals(self,  p):
        # if the numbe of goals is equal, less played games is better
        return (p['goals'], -p['games'])
 
    def player_data(self, name: str):
        for player in self.__players:
            if player['name'] == name:
                return player
 
        return None
 
    def countries(self):
        return sorted(list(set(p['nationality'] for p in self.__players )))
 
    def teams(self):
        return sorted(list(set(p['team'] for p in self.__players )))
 
    def players_in_team(self, team: str):
        players = [ p for p in self.__players if p['team'] == team]
        return sorted(players, key=self.by_points, reverse=True)
 
    def players_from_country(self, country: str):
        players = [ p for p in self.__players if p['nationality'] == country]
        return sorted(players, key=self.by_points, reverse=True)
 
    def most_points(self, countryra):
        players = sorted(self.__players, key=self.by_points, reverse=True)
        return players[0: countryra]
 
    def most_goals(self, countryra):
        players = sorted(self.__players, key=self.by_goals, reverse=True)
        return players[0: countryra]
 
class Application:
    def __init__(self):
        self.__statistics = None
 
    def instructions(self):
        instructions = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(instructions)
 
    def f(self, p: dict):
        """
            helper method, which creates a string out of players formatted for output
        """
        points = p['goals'] + p['assists']
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
 
    def read_file(self):
        file_name = input("file: ")
        with open(file_name) as file:
            data = file.read()
 
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.__statistics = Statistics(players)
 
    def get_playes(self):
        name = input("name: ")
        player = self.__statistics.player_data(name)
        if player:
            print(self.f(player))
 
    def get_teams(self):
        for team in self.__statistics.teams():
            print(team)
 
    def get_countries(self):
        for country in self.__statistics.countries():
            print(country)
 
    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(self.f(player)) 
 
    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(self.f(player)) 
 
    def most_points(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_points(number):
            print(self.f(player)) 
 
    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_goals(number):
            print(self.f(player)) 
 
    def execute(self):
        self.read_file()
        self.instructions()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.get_playes()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
 
Application().execute()
'''

