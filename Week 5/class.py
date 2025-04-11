# Base class
class FootballTeam:
    def __init__(self, name, coach, ranking):
        self.name = name
        self.coach = coach
        self.ranking = ranking

    def display_info(self):
        print(f"Team: {self.name} | Coach: {self.coach} | Ranking: {self.ranking}")

    def train(self):
        print(f"{self.name} is training hard 💪")

# Child class with encapsulation
class InternationalTeam(FootballTeam):
    def __init__(self, name, coach, ranking, country):
        super().__init__(name, coach, ranking)
        self.__country = country  # encapsulated attribute

    def display_country(self):
        print(f"{self.name} represents {self.__country} 🌍")

# Creating team objects
team1 = FootballTeam("Manchester United", "Ruben Amorim", 13)
team2 = InternationalTeam("Harambee Stars", "Benni McArthy", 110, "Kenya")

team1.display_info()
team1.train()

print("")

team2.display_info()
team2.train()
team2.display_country()
