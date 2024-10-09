def square_number5(n):

    base = n // 10
    print(base)
    result = base * (base + 1)
    print(result)

    return int(f"{result}25")


with open('INPUT.TXT', 'r') as file:
    n = int(file.read().strip())

result = square_number5(n)

with open('OUTPUT.TXT', 'w') as file:
    file.write(str(result))


print(4255//10)
print(425*426)
print(4255*4255)