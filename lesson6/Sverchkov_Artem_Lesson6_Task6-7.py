# HW_Lesson6_Task6-7
# Add
import sys
price = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as file:
    file.write(price + '\n')

# Show
import sys
price = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as file:
    if len(price) == 0:
        start_idx = 0
        end_idx = 0
        for line in file:
            end_idx += 1
        file.seek(0)
    elif len(price) > 1:
        start_idx = int(price[0])
        end_idx = int(price[1])
    else:
        start_idx = int(price[0])
        end_idx = 0
        for line in file:
            end_idx += 1
    file.seek(0)
    for idx, line in enumerate(file):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())

# Replace
import sys

edit_idx, new_val = sys.argv[1:]
with open('bakery.csv', 'r+') as file:
    tmp_file = open('bakery.tmp', 'w+')
    change = False
    for i, line in enumerate(file, 1):
        if i == int(edit_idx):
            tmp_file.write(f'{new_val}\n')
            change = True
        else:
            tmp_file.write(line)
    if not change:
        exit('error')

    tmp_file.seek(0)

    file.truncate(0)
    for line in tmp_file:
        file.write(line)
    tmp_file.close()