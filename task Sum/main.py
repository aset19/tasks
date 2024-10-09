# with open('input.txt', 'r') as input_file:
#     number = int(input_file.readline())
# if number >= 1:
#       result = (number + (number+1))//2
#       print(result)
# else:
#      result = ((1 + number) * (abs(number) + 1)) // 2



with open('INPUT.TXT', 'r') as input_file:
    N = int(input_file.readline().strip())

if N >= 1:
    # Сумма чисел от 1 до N
    result = N * (N + 1) // 2
else:
    # Сумма чисел от 1 до N, когда N <= 0
    result = ((N * (N - 1)) // 2) + 1

# Записываем результат в файл OUTPUT.TXT
with open('OUTPUT.TXT', 'w') as output_file:
    output_file.write(str(result))