print()

## Part 2 Example
# scratchoff_cards = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#                     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#                     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#                     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#                     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#                     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

# Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
# Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
# Your copy of card 2 also wins one copy each of cards 3 and 4.
# Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
# Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
# Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
# Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

# Once all of the originals and copies have been processed, you end up with:
#  1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 
# 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. 
# In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

with open('2023/Day 4 Scratchcards/input_text.txt', 'r') as file:
    scratchoff_cards = file.read().splitlines()

card_counting_dict = {}
for i in range(1, len(scratchoff_cards)+1):
    card_counting_dict[i] = 1

scratchoff_cards = [x[x.index(': ')+2:] for x in scratchoff_cards]
scratchoff_cards = [x.split(' | ') for x in scratchoff_cards]
scratchoff_cards = [x.split(' ') for y in scratchoff_cards for x in y]

winning_numbers_counter = 0
point_total = 0

for i in range(0,len(scratchoff_cards), 2):
    current_card = (i//2)+1
    winning_numbers_counter = set(scratchoff_cards[i]).intersection(set(scratchoff_cards[i+1]))

    if '' in winning_numbers_counter:
        winning_numbers_counter.remove('')

    winning_numbers_counter = len(winning_numbers_counter)

    #print(f"{current_card}: {[current_card+x for x in range(1,winning_numbers_counter+1) ]}")

    for adder in range(1,winning_numbers_counter+1):
        card_counting_dict[current_card+adder] += 1*card_counting_dict[current_card]
        #print(f"Number of instances of card {current_card+adder}: {card_counting_dict[current_card+adder]}")


print(f"Answer: {sum(card_counting_dict.values())}")
print()



