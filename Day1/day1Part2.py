import day1Part1_functions as d1p1
import re


def find_left_and_right_value(input_string):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    table = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    table_reverse = {'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'}
    total_sum = 0
    replace = {'zerone' : "zeroone", "oneight" : "oneeight", "twone" : "twoone", "sevenine" : "sevennine", "eightwo" : "eighttwo", "eighthree" : "eightthree", "nineight" : "nineeight"}
    newlist = []
    afterlist = []

    lines = input_string.strip().split('\n')

    #First, replace all the anomaly using replace dictionary, then add the new values to newlist
    for line in lines:
        for replacement in replace:
            if replacement in line:
                rp = replace[replacement]
                line = line.replace(replacement, rp)   
        newlist.append(line)

    #Creates a new list           
    pointer = 0
    #Replace the strings from table from text to numbers.
    for char in newlist:
        for word, value in table.items():
            char = char.replace(word, value)
            pointer+=1
        afterlist.append(char)

    print(afterlist)

    pointerleft = 0
    pointerright = -1
    #Picking the most left number as first digit.
    for char in afterlist:
        pointerleft = 0
        pointerright = len(char) - 1  # Set pointerright to the last index of the string
        while pointerleft < len(char) and not char[pointerleft].isdigit():
            pointerleft += 1  # Move pointerleft to the next digit if it's not a digit

        while pointerright >= 0 and not char[pointerright].isdigit():
            pointerright -= 1  # Move pointerright to the previous digit if it's not a digit

        # Check if both pointers are valid indices
        if pointerleft < len(char) and pointerright >= 0:
            keyleft = char[pointerleft]
            keyright = char[pointerright]

            # Add to the sum.
            total_sum += int(str(keyleft) + str(keyright))
    return total_sum

    


#main
result = find_left_and_right_value(d1p1.values)
print(result)
