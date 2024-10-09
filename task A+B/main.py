
with open('input.txt', 'r') as input_file:
    numbers = input_file.readline().split()
    print(numbers)
    A = int(numbers[0])
    print('A=',A)
    B = int(numbers[1])
    print('B=', B)


result = A + B
with open('OUTPUT.TXT', 'w') as output_file:
    output_file.write(str(result))
