from deck import Deck
import os
import matplotlib.pyplot as plt

def compute_score(cards):

    score = 0

    for card in cards:
        value = card[:-1]
        if value in ['J', 'Q', 'K']:
            score += 10
        elif value == 'A':
            if score > 9:
                score += 1
            else:
                score += 11
        else:
            score += int(value)

    return score

def logic(player_cards, dealer_card):

    # Get the player's current point total
    player_score = compute_score(player_cards)

    # Get the dealer's current point total
    dealer_val = dealer_card[:-1]
    if dealer_val == 'A':
        dealer_score = 11
    elif dealer_val in ['10', 'J', 'Q', 'K']:
        dealer_score = 10
    else:
        dealer_score = int(dealer_val)


    # Implement the hit or stay logic
    if player_score == 11:
        return 'hit'
    elif player_score == 12:
        if dealer_score >=4 and dealer_score <= 6:
            return 'stay'
        else:
            return 'hit'
    elif player_score >= 13 and player_score <= 16:
        if dealer_score >= 7:
            return 'hit'
        else:
            return 'stay'
    else:
        return 'stay'

def dealer_logic(cards):

    dealer_score = compute_score(cards)

    if dealer_score >= 17:
        return 'stay'
    else:
        return 'hit'

def decide_winner(player, dealer):

    # Compute player score
    player_score = compute_score(player)

    # Compute dealer score
    dealer_score = compute_score(dealer)

    # If player busted, dealer wins
    if player_score > 21:
        return 'lose'

    # If dealer busted, player wins
    if dealer_score > 21:
        return 'win'

    # If neither busted, then whoever has the highest score wins
    if player_score > dealer_score:
        return 'win'
    elif dealer_score > player_score:
        return 'lose'
    else:
        return 'tie'

def play():

    # Clear the terminal for a clean output
    # os.system('clear')

    # Keep this as true while the player can still make decisions
    player_playing = True

    # Create a shuffled deck
    deck = Deck()

    # Give player and dealer their cards
    player = []
    dealer = []

    player.append(deck.deal_ten())
    player.append(deck.deal_card())
    dealer.append(deck.deal_card())
    dealer.append(deck.deal_card())

    # print("Player's cards: " + player[0] + " " + player[1])
    # print("Dealer's card: " + dealer[0])

    player_score = compute_score(player)

    if player_score == 21:
        return 'win'

    # print()

    while player_playing:

        decision = logic(player, dealer[0])
        # print(decision)

        # If the player hits, deal them another card
        if decision == 'hit':
            player.append(deck.deal_card())

        # If the player stay's then they are not allowed to make any more moves
        else:
            player_playing = False

    # print("Player's final cards:", player)

    # Implement dealer logic
    dealer_playing = True
    while dealer_playing:
        decision = dealer_logic(dealer)

        # If the dealer hits, deal them a new card
        if decision == 'hit':
            dealer.append(deck.deal_card())

        # If the dealer stays, end the loop
        else:
            dealer_playing = False
    # print("Dealer's cards:", dealer)


    return decide_winner(player, dealer)

def plot_scores(scores):

    # the histogram of the data
    n, bins, patches = plt.hist(scores, density=True, alpha=0.75)

    # plt.xlabel('Smarts')
    # plt.ylabel('Probability')
    # plt.title('Histogram of IQ')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.xlim(40, 160)
    # plt.ylim(0, 0.03)
    plt.grid(True)
    plt.show()

def main():

    num_games = 10000

    wins = 0
    losses = 0

    for i in range(num_games):
        result = play()
        if result == 'win':
            wins += 1
        else:
            losses += 1

    print("Wins:", "{0:.4%}".format(wins/num_games))
    print("Loses:", "{0:.4%}".format(losses/num_games))

if __name__ == "__main__":
    main()
