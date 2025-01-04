def card_value(card):
    """Returns the value of a single card."""
    if card in ['K', 'Q', 'J', 'T', 'A']:
        return 10
    else:
        return int(card)

def f(player1, player2):
    set1 = list(player1)
    set2 = list(player2)
    """Returns True if player1 has cards of the same or higher value than player2, False otherwise."""
    total_player1 = sum(card_value(card) for card in set1)
    total_player2 = sum(card_value(card) for card in set2)
    
    return total_player1 >= total_player2

# Example usage:
player1 = "AJ972"
player2 = "134"

print(f(player1, player2))  # Output: True

    