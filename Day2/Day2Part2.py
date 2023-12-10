import Day2_input as d2in

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
        red = 0
        blue = 0
        green = 0
        print(f"Game: {gamecount}")
        for cause in games.split(';'):
            for cubes in cause.split(','):
                num, color = cubes.split()
                num = int(num)  
                if color == 'red' and num > red:
                    red = num
                elif color == 'blue' and num > blue:
                    blue = num
                elif color == 'green' and num > green:
                    green = num
        print(f"Highest Red = {int(red)}")
        print(f"Highest Blue = {int(blue)}")
        print(f"Highest Green = {int(green)}")

        total = red * blue * green
        print(f"Total from game {gamecount} is {total}")
        thenuts += total

              
    print("Sum of cubes: ")                
    print(thenuts)



sum = check_colors(game)
#print(sum)
