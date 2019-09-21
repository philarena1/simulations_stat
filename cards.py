from random import randint

def generate_deck(num_of_deck):
	suits = ['H','S','C','D']
	numbs = list(range(2,11))

	faces = ['J','Q','K','A']

	deck = numbs + faces

	full_deck = []
	for suit in suits:
	    for card in deck:
	        full_deck.append(str(card) + suit)

	num_decks = num_of_deck
	total_decks = full_deck * num_decks

	return total_decks


decks = generate_deck(10)
print(decks)
