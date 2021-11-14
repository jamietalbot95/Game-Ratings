games = []
new_game = []


class Leaderboard:
    def __init__(self,board):
        self.board = board

    def display_top_5(self):
        print("\nThe top 5 games are:\n")
        for i in range(0,5):
            try:
                lines = self.board[i]
                print(f"{i+1}: {lines[0]} - {lines[1]} - {lines[2]}")
            except IndexError:
                continue

    def sort_board(self):
        for i in range(1, len(self.board)):
            value = self.board[i][2]
            game = self.board[i]
            j = i - 1
            while j >= 0 and self.board[j][2] < value:
                self.board[j + 1] = self.board[j]
                j = j - 1
            self.board[j + 1] = game
        return self.board


def display_menu():
    print("\n1. Enter new game details\n"
          "2. Update game sales figures\n"
          "3. Remove game\n"
          "4. Print chart\n"
          "5. Quit")


def generate_top_5():
    all_scores = []
    top_5_scores = [0, 0, 0, 0, 0]
    for game in games:
        all_scores.append(int(game[2]))
    i = 0
    while i <= 5:
        try:
            all_scores.sort(reverse=True)
            top_5_scores[i] = int(all_scores[i])
            top_5_scores.sort(reverse=True)
            i += 1
        except IndexError:
            break
    return top_5_scores


def check_in_top_5(score):
    top_5 = generate_top_5()
    if score < top_5[4]:
        return False
    else:
        return True


def enter_new_game():
    new_game = input("Please input the game title, the publisher and the total sales - all separated by commas:").split(",")
    new_game[2] = int(new_game[2])
    games.append(new_game)
    if check_in_top_5(int(new_game[2])):
        print("\nScore is high enough to be in the top 5")
    else:
        print("\nScore isn't high enough to be in the top 5, but has been stored so the game can be updated later.")


def update_game():
    game_to_update = input("Please enter the game you would like to update: ")
    score_to_update = int(input("What is the new sale total?"))
    score_updated = False
    for i in range(0,len(games)):
        if games[i][0] == game_to_update:
            games[i][2] = score_to_update
            score_updated = True
    if score_updated:
        print("\nScore updated")
    else:
        print("\nCouldn't find that game, did you enter it correctly?")


def remove_game():
    game_to_remove = input("Please enter the game you would like to remove: ")
    for i in range(0,len(games)-1):
        if games[i][0] == game_to_remove:
            games.pop(i)


def main_loop():
    quit_program = False
    while not quit_program:
        display_menu()
        function_selection = input("Please enter your choice of function: ")
        if function_selection == "1":
            enter_new_game()
        elif function_selection == "2":
            update_game()
        elif function_selection == "3":
            remove_game()
        elif function_selection == "4":
            board = Leaderboard(games)
            board.sort_board()
            board.display_top_5()
        elif function_selection == "5":
            quit_program = True


main_loop()


