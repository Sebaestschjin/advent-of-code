from . import reader

TOTAL_GAMES = 0


class Game:
    def __init__(self, decks, recursive=False, depths=0):
        self.decks = decks
        self.recursive = recursive
        self.played_rounds = []
        self.round = 0
        self.depths = depths + 1
        global TOTAL_GAMES
        TOTAL_GAMES += 1
        self.game_number = TOTAL_GAMES

    def play_till_end(self):
        while not self.determine_winner():
            self.round += 1
            self.play_round()
        return self.determine_winner()

    def play_round(self):
        self.played_rounds.append((self.decks[0].copy(), self.decks[1].copy()))

        first_deck, second_deck = self.decks
        first_card = first_deck.pop(0)
        second_card = second_deck.pop(0)

        winner = self.determine_winner_of_round(first_card, second_card)

        if winner == 0:
            first_deck.append(first_card)
            first_deck.append(second_card)
        else:
            second_deck.append(second_card)
            second_deck.append(first_card)

    def determine_winner_of_round(self, first_card, second_card):
        if self.require_sub_game(first_card, second_card):
            sub_game = Game((self.decks[0][:first_card].copy(),
                             self.decks[1][:second_card].copy()),
                            recursive=True, depths=self.depths)
            winner = sub_game.play_till_end()[0]
            return winner
        else:
            return 0 if first_card > second_card else 1

    def require_sub_game(self, first_card, second_card):
        return self.recursive and len(self.decks[0]) >= first_card and len(self.decks[1]) >= second_card

    def determine_winner(self):
        first_deck, second_deck = self.decks

        if self.recursive and self.decks in self.played_rounds:
            return 0, first_deck
        if not first_deck:
            return 1, second_deck
        if not second_deck:
            return 0, first_deck
        return None

    def __eq__(self, other):
        return self.decks == other.decks

    def __hash__(self):
        return hash(self.decks)


def calculate_score(deck):
    total = 0
    deck = deck[::-1]
    for i in range(len(deck)):
        total += (i + 1) * deck[i]
    return total


def solve_a(decks):
    reset_games()
    game = Game(decks)
    _, winning_deck = game.play_till_end()
    return calculate_score(winning_deck)


def solve_b(decks):
    reset_games()
    game = Game(decks, recursive=True)
    _, winning_deck = game.play_till_end()
    return calculate_score(winning_deck)


def reset_games():
    global TOTAL_GAMES
    TOTAL_GAMES = 0


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
