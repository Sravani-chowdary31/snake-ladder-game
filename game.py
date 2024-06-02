import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

class Board:
    def __init__(self):
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def check_position(self, position):
        if position in self.snakes:
            return self.snakes[position], 'snake'
        elif position in self.ladders:
            return self.ladders[position], 'ladder'
        return position, None

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.consecutive_sixes = 0

class Game:
    def __init__(self, num_players):
        self.board = Board()
        self.dice = Dice()
        self.players = [Player(f'Player {i+1}') for i in range(num_players)]
        self.current_player_index = 0

    def play_turn(self, player):
        roll = self.dice.roll()
        print(f"{player.name} rolled a {roll}")

        if roll == 6:
            player.consecutive_sixes += 1
            if player.consecutive_sixes == 3:
                print(f"{player.name} rolled three consecutive sixes! Returning to position before the sixes.")
                player.position -= 12
                player.consecutive_sixes = 0
                return
        else:
            player.consecutive_sixes = 0

        start_position = player.position
        player.position += roll

        if player.position > 100:
            player.position = 100

        new_position, entity = self.board.check_position(player.position)
        if entity == 'snake':
            print(f"{player.name} encountered a snake! Sliding down to {new_position}.")
        elif entity == 'ladder':
            print(f"{player.name} climbed a ladder! Moving up to {new_position}.")
        
        player.position = new_position
        print(f"{player.name} moved from {start_position} to {player.position}")

    def has_winner(self):
        for player in self.players:
            if player.position == 100:
                print(f"{player.name} has won the game!")
                return True
        return False

    def next_player(self):
        if self.players[self.current_player_index].consecutive_sixes < 3:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_game(self):
        while not self.has_winner():
            current_player = self.players[self.current_player_index]
            self.play_turn(current_player)
            self.next_player()

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    game = Game(num_players)
    game.play_game()
