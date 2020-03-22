import time
import math

time_1 = time.time()
value_1 = 999
value_2 = 999
found_answer = False
answer_list = [0]
while value_1 > 99 and value_2 > 99:
    test_value = value_1 * value_2
    is_palindrome = True
    for i in range(math.floor(len(str(test_value)) / 2)):
        if str(test_value)[i] != str(test_value)[-1 * (i + 1)]:
            is_palindrome = False
            break
    if is_palindrome is True:
        answer_list.append(test_value)
    if value_2 == 100 or test_value < max(answer_list):
        value_1 -= 1
        value_2 = value_1
    else:
        value_2 -= 1
answer = max(answer_list)
print(answer)
print(time.time() - time_1)