import Day2_input as d2in

#The Elf would first like to know which games would have been possible 
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#Max = 12 red, 13 green, 14 blue.
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue


game = d2in.record.strip()
count = 0

def check_colors(string):
    gamecount = 0
    thenuts = 0
    possiblegames_sum = 0
    bonkers = False
    for games in game.split('\n'):
        game_num, games = games.split(':')
        bonkers = False
        gamecount+=1
        possiblegames_sum += gamecount
        num_fails = 0
        print(f"Game: {gamecount}")
        for cause in games.split(';'):
            for cubes in cause.split(','):
                num, color = cubes.split()
                if int(num) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    print(num, color)
                    bonkers = True
                    num_fails += 1
                    #print(f"Num Fails: {num_fails}")

        if bonkers == False:
            thenuts += int(game_num.split()[-1])

              
    print("Sum of possible games: ")                
    print(thenuts)








sum = check_colors(game)
#print(sum)

