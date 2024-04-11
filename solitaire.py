import random

# Initialize the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Deal cards to tableau
tableau = [deck[i:i+7] for i in range(0, 28, 7)]
for pile in tableau:
    pile[-1]['face_up'] = True

# Initialize foundation piles
foundation = {suit: [] for suit in suits}

# Display the tableau and foundation
def display_board():
    print("Tableau:")
    for i, pile in enumerate(tableau):
        print(f"{i + 1}: ", end="")
        for card in pile:
            if card.get('face_up'):
                print(f"{card['rank']} of {card['suit']}, ", end="")
            else:
                print("Face down, ", end="")
        print()
    print("\nFoundation:")
    for suit, pile in foundation.items():
        print(f"{suit}: ", end="")
        for card in pile:
            print(f"{card['rank']} of {card['suit']}, ", end="")
        print()

# Main game loop
def main():
    display_board()
    while True:
        action = input("\nEnter your action (q to quit): ").lower()
        if action == 'q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
