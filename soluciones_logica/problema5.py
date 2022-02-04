#!/usr/bin/python3

bottom_right_result = 3
bottom_left_result = 5
upper_left_result = 7
upper_right_result = 9
total_result = 1    

for i in range(1, 3):
    bottom_right_result = bottom_right_result + 2 + 8 * i
    bottom_left_result = bottom_left_result + 4 + 8 * i
    upper_left_result = upper_left_result + 6 + 8 * i
    upper_right_result = upper_right_result + 8 + 8 * i
    total_result = total_result + bottom_right_result + bottom_left_result + upper_left_result + upper_right_result

print(total_result)
