class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def display_player(self):
        print(f"Player: {self.name}, Level: {self.level}")

    @classmethod
    def get_total_players(cls):
        print(f"Total players created: {cls.player_count}")

p1 = Player("Alpha", 5)
p2 = Player("Bravo", 10)
p3 = Player("Charlie", 1)

p1.display_player()
p2.display_player()
p3.display_player()

Player.get_total_players()