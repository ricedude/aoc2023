import day1Part1_functions as d1p1
import re

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def numerical_extract(string_data):
    lines = string_data.strip().split('\n')
    total_sum = 0
    pointer = 0
    pointerleft = 0
    pointerright = -1
    for line in lines:
        while str(lines[pointer][pointerleft]) not in numbers:
            pointerleft+=1
        
        keyleft = lines[pointer][pointerleft]

        while str(lines[pointer][pointerright]) not in numbers:
            pointerright-=1

        keyright = lines[pointer][pointerright]

        total_sum += int(str(keyleft) + str(keyright))
        print(total_sum)
        pointer+=1
        pointerleft = 0
        pointerright = -1
    return total_sum


    



result = numerical_extract(d1p1.values)
print(result)