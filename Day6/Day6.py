#Pseudocode:
# Make time array using split.
# so time[] will have 7, 15, 30 and for each race it goes up.
# so distance[] will have 9 40 200 and for each race it will go up.

# charging the speed of the boat gives 1 ms per ms increase, but it wont move.

# win_array = []
# i = -1
# for t in time:
#   i +=1 
#   for increase in range(t):
#       #Button hold is increase.
#       #starts at 0
#       remaining_time = t - increase
#       if increase > 0:
#           speed+= 1
#       travel_distance = remaining_time * speed
#       if travel_distance > distance[i]:
#           ways_to_win += 1
# win_array.append(ways_to_win)
# then times all win_array values together.

time = []
distance = []

#Stripping the input.txt
with open(r'C:\Users\deadi\OneDrive\Documents\Python\AdventofCode\Day6\input.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith('Time: '):
            for num in line.split()[1:]:
                time.append(num)
                continue
        if line.startswith('Distance: '):
            for num in line.split()[1:]:
                distance.append(num)

#Part 1
win_array = []
i = -1
for t in time:
    speed = 0
    ways_to_win = 0
    i +=1 
    travel_distance = 0
    for increase in range(int(t)):
    #Button hold is increase.
    #starts at 0
        remaining_time = int(t) - increase
        if increase > 0:
            speed+= 1
            travel_distance = remaining_time * speed
        if travel_distance > int(distance[i]):
            ways_to_win += 1
    win_array.append(ways_to_win)


def sum_cal(list):
    result = 1
    for num in list:
        result *= num
    return result

print(f"The total sum for part 1 is: {sum_cal(win_array)}")

#Part 2
#combine all the time and distance into 1 value

total_time = ""
total_distance = ""
for t in time:
    total_time = str(total_time) + t
for d in distance:
    total_distance = str(total_distance) + d

print(total_time)
print(total_distance)

speed = 0 
ways_to_win = 0
for increase in range(int(total_time)):
#Button hold is increase.
#starts at 0
    remaining_time = int(total_time) - increase
    if increase > 0:
        speed+= 1
        travel_distance = remaining_time * speed
    if travel_distance > int(total_distance):
        ways_to_win += 1

print(f"The total sum for part 2 is: {ways_to_win}")