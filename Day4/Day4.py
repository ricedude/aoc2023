numbers =[]

with open(r'C:\Users\deadi\OneDrive\Documents\Python\AdventofCode\Day4\input.txt', 'r') as f:
    for line in f.readlines():
        numbers.append(line.strip())

#cleaned_text = [line[line.find(": ") + 1:] for line in numbers]

num = []
win_num = []

for line in numbers:
    if line.strip():  # Check if the line is not empty
        parts = line.split(' | ')
        card_number, win_numbers = parts[0].split(': ')[1], parts[1]
        num.append(card_number)
        win_num.append(win_numbers)


#print(num)
#print(win_num)

seq = 0
target_num = 0
first = 0
i = -1
points = 0
total_points = 0


#Part 1
"""
for i, card in enumerate(num):
    print(card)
    card_numbers = card.split()
    for num in card_numbers:
        matched = False
        for win_card in win_num[i].split():
            if num == win_card:
                print(f"{num} in card {i + 1} matched.")
                if points < 2:
                    points += 1
                else:
                    points *= 2
    total_points += points
    points = 0

print(f"Total points: {total_points}")
"""

#Part 2
all_cards = {}
correct_cards = []

j = 0

#Return total number of matches for each card.
for i in range(len(win_num)):
    for char in win_num[i].split():
        for n in num[i].split():
            if char == n:
                j = j + 1
    correct_cards.append(j)
    j = 0

print(correct_cards)
num_cards = [1 for _ in correct_cards]
for i, correct_cards in enumerate(correct_cards):
    for n in range(correct_cards):
        num_cards[i+1+n] += num_cards[i]

print(num_cards)
print(sum(num_cards))
    


print("End. ")