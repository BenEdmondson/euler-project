import time

time_1 = time.time()
single_dict = {'0': '',
               '1': 'one',
               '2': 'two',
               '3': 'three',
               '4': 'four',
               '5': 'five',
               '6': 'six',
               '7': 'seven',
               '8': 'eight',
               '9': 'nine'}
tens_dict = {'2': 'twenty',
             '3': 'thirty',
             '4': 'forty',
             '5': 'fifty',
             '6': 'sixty',
             '7': 'seventy',
             '8': 'eighty',
             '9': 'ninety'}
awkward_tens_dict = {'0': 'ten',
                     '1': 'eleven',
                     '2': 'twelve',
                     '3': 'thirteen',
                     '4': 'fourteen',
                     '5': 'fifteen',
                     '6': 'sixteen',
                     '7': 'seventeen',
                     '8': 'eighteen',
                     '9': 'nineteen'}
total_letters = 0
for i in range(1, 1001):
    word = ''
    if len(str(i)) >= 4:
        digit = str(i)[-4]
        word += single_dict[digit] + 'thousand'
    if len(str(i)) >= 3:
        digit = str(i)[-3]
        if digit != '0':
            word += single_dict[digit] + 'hundred'
    if len(str(i)) >= 2:
        digit = str(i)[-2]
        second_digit = str(i)[-1]
        if len(str(i)) >= 3 and not (digit == '0' and second_digit == '0'):
            word += 'and'
        if digit == '0':
            word += single_dict[second_digit]
        elif digit == '1':
            word += awkward_tens_dict[second_digit]
        else:
            word += tens_dict[digit]
            word += single_dict[second_digit]
    else:
        digit = str(i)[-1]
        word += single_dict[digit]
    print(str(i), word)
    total_letters += len(word)

print(total_letters)
print(time.time() - time_1)