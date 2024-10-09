
with open('INPUT.TXT', 'r') as file:
    data = file.read().strip().split()
    print(data)

    A = int(data[0])
    B = int(data[1])
    C = int(data[2])

if A * B == C:
    result = "YES"
else:
    result = "NO"

with open('OUTPUT.TXT', 'w') as file:
    file.write(result)
