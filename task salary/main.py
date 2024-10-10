

with open('input.txt', 'r') as input_file:
    salary = [int(i) for i in input_file.read().strip().split() ]
    min_salary = []
    min_salary.append(max(salary) - min(salary))



with open('output.txt', 'w') as output_file:
    output_file.write(''.join(map(str,min_salary)) + '\n')
