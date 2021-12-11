import time
import copy

class BingoCard:
    def __init__(self, card_values):
        self.card_values = card_values
    
    def __str__(self):
        string_rep = ""
        for line in self.card_values:
            string_rep += str(line) + "\n"
        return string_rep
    
    def mark_card(self, called_number):
        for i in range(len(self.card_values)):
            for j in range(len(self.card_values[i])):
                if self.card_values[i][j] == called_number:
                    self.card_values[i][j] = "X"

    def check_win_cond(self):
        # check columns for win condition
        for i in range(0, 5):
            # Check row for win condition
            if all(element == "X" for element in self.card_values[i]):
                return True

            # Check columns for win condition
            column_matches = True
            for j in range(0, 5):
                if(self.card_values[j][i] != "X"):
                    column_matches = False
                    break;
            if(column_matches):
                return True

        return False

    def calculate_score(self, last_called):
        print("FOUND WINNER")
        print(self)
        score = 0
        for row in self.card_values:
            for number in row:
                if number != "X":
                    score += int(number)
        return score * int(last_called)

def importData(filename):
    # Reads data from input file
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.strip() for line in input if line.strip() != ""]

    # Removes number call order from list
    call_order = input[0].split(",")
    del input[0]

    bingo_cards = []
    two_d_card = []
    count = 0

    for i in range(len(input)):
        two_d_card.append(input[i].split())
        count += 1
        if(count == 5):
            bingo_cards.append(BingoCard(copy.deepcopy(two_d_card)))
            two_d_card.clear()
            count = 0

    return [call_order, bingo_cards]

def find_winner(cards, call_order):
    for number in call_order:
        for card in cards:
            card.mark_card(number)
            if(card.check_win_cond() == True):
                return card.calculate_score(number)

def find_last_winner(cards, call_order):
    for number in call_order:
        print("NUMBER CALLED: " + number)
        for card in cards:
            card.mark_card(number)
            print(card)
            if(card.check_win_cond() == True):
                if (len(cards) > 1):
                    cards.remove(card)
                else:
                    return card.calculate_score(number)

data = importData("Day 4 Giant Squid\input.txt")
call_order, cards = data[0], data[1]

test_data = importData("Day 4 Giant Squid\testinput.txt")
test_call_order, test_cards = test_data[0], test_data[1]


print("--------------------------------------")
print("DAY FOUR: GIANT SQUID")
print("Part One Answer: " + str(find_winner(cards, call_order)))
print("Part Two Answer: " + str(find_last_winner(test_cards, test_call_order)))
print("--------------------------------------")
