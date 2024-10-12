with open('INPUT.TXT', 'r') as input_file:
    num = [int(i) for i in input_file.read().strip().split()]
    print(num[0])
    print(num[1])
    print(num[0] > num[1])

    with open('OUTPUT.TXT', 'w') as output_file:
        if num[0] > num[1]:
            output_file.writelines(f'>')
        elif num[0] < num[1]:
            output_file.writelines(f'<')
        else:
            output_file.writelines(f'=')





# output_file.writelines(f'{num[0]}={num[1]}')