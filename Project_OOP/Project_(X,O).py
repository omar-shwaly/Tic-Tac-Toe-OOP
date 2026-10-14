# class player #
# ***************** #
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):

        while True:
            name = input("Enter your name  (letters only..)\n")
            if name.isalpha() == True:
                self.name = name
                break

            else:
                print("Invalid name , plase letters only")

    def choose_symbol(self):

        while True:
            symbol = input(f"{self.name} chosse your symbol a(string letter) \n")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()

                break
            else:
                print("Invalid symbol , plase letters only")


# class Menu#
# ***************** #
class Menu:

    def disblay_main_menu(self):

        print("#" * 50)
        print("Welcom to my X-o game!")
        print("#" * 50)
        print("1.Start Game")
        print("2. Quit Game")
        print("#" * 50)

        choice = int(input("Enter your choice (1 or 2)  \n"))
        if choice == 1 or choice == 2:
            return choice

        if choice > 2 or choice < 1:
            print("Invalid choise , plase enter choise agin (1 or 2)")

    def disblay_endgame_menu(self):
        # Multiline String

        menu_text = """
Game over!
1. Restart Game
2. Quit Game 
Enter your choice (1 or 2) """

        choice = int(input(menu_text + "\n"))
        if choice == 1 or choice == 2:
            return choice

        if choice > 2 and choice < 1:
            print("Invalid choise , plase enter choise agin (1 or 2)")


# class Board #
# ***************** #
class Board:

    def __init__(self):

        self.board = []
        for i in range(1, 10):
            self.board.append(str(i))

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i : i + 3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, option, symbol):

        if self.is_avild_move(option):

            self.board[option - 1] = symbol
            return True
        else:
            return False

    def is_avild_move(self, option):

        if self.board[option - 1].isdigit() == True:

            return True

        else:
            return False

    def reset_board(self):
        self.board = []
        for i in range(1, 10):
            self.board.append(str(i))


# class Game #
# ***************** #
class Game:

    def __init__(self):

        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()

        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.disblay_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details")
            player.choose_name()
            player.choose_symbol()
            print("-" * 20)

    def quit_game(self):
        print("Thank you for playing")

    def play_game(self):
        while True:
            self.play_turn()

            if self.check_win():
                self.board.display_board()
                winner = self.players[self.current_player_index]
                print(f"Congratulations ! {self.winner.name} wins!")

            if self.check_win() or self.check_draw():
                choice = self.menu.disblay_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name} is turn ({player.symbol})")

        while True:
            try:
                cell_choice = int(input("choose a cell (1-9):\n"))
                if 1 <= cell_choice <= 9 and self.board.update_board(
                    cell_choice, player.symbol
                ):
                    self.winner = player
                    break
                else:
                    print("Invalid move , try again")

            except ValueError:
                print("please enter a number between 1 and 9")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_cobinations = [
            # rows
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            # colums
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            # diagn
            [0, 4, 8],
            [2, 4, 6],
        ]

        for combo in win_cobinations:
            if (
                (self.board.board[combo[0]])
                == self.board.board[combo[1]]
                == self.board.board[combo[2]]
            ):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()


game = Game()
game.start_game()
