with open('input.txt', 'r') as input_file:
    num = int(input_file.read())
    list_num = [num,9,9-num]
with open('output.txt', 'w') as output_file:
    output_file.write(''.join(map(str,list_num)))