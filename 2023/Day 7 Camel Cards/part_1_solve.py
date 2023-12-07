from collections import Counter
print()

## Part 1 Example
# camel_cards = [ "32T3K 765",
#                 "T55J5 684",
#                 "KK677 28",
#                 "KTJJT 220",
#                 "QQQJA 483"]

with open('2023/Day 7 Camel Cards/input_text.txt', 'r') as file:
    camel_cards = file.read().splitlines()

camel_cards = [x.split() for x in camel_cards]

my_dict = { "A" : "A",
            "K" : "B",
            "Q" : "C",
            "J" : "D",
            "T" : "E",
            "9" : "F",
            "8" : "G",
            "7" : "H",
            "6" : "I",
            "5" : "J",
            "4" : "K",
            "3" : "L",
            "2" : "M"}

hand_type_dict = {'five_of_a_kind'  : [],
                  'four_of_a_kind'  : [],
                  'full_house'      : [],
                  'three_of_a_kind' : [],
                  'two_pair'        : [],
                  'one_pair'        : [],
                  'high_card'       : []
                  }

rank = len(camel_cards)

for hand, bet in camel_cards:
    
    for key, value in my_dict.items():
        hand = hand.replace(key, value)

    # print(f"Hand: {hand} || Bet: {bet} || Count: {Counter(hand).values()}")

    hand_counts = Counter(hand).values()

    if 5 in hand_counts:
        hand_type_dict['five_of_a_kind'].append((hand, bet))
    elif 4 in hand_counts:
        hand_type_dict['four_of_a_kind'].append((hand, bet))
    elif (3 in hand_counts) and (2 in hand_counts):
        hand_type_dict['full_house'].append((hand, bet))
    elif (3 in hand_counts) and (2 not in hand_counts):
        hand_type_dict['three_of_a_kind'].append((hand, bet))
    elif Counter(hand_counts)[2] == 2:
        hand_type_dict['two_pair'].append((hand, bet))
    elif Counter(hand_counts)[2] == 1:
        hand_type_dict['one_pair'].append((hand, bet))
    else:
        hand_type_dict['high_card'].append((hand, bet))


for k, v in hand_type_dict.items():
    v.sort(key=lambda a: a[0])


total_winnings = 0
for h_type in ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']:
    for v in hand_type_dict[h_type]:
        
        total_winnings += int(v[1]) * rank
        rank -= 1

print(f"Answer: {total_winnings}")
print()





    

