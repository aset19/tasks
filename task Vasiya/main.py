with open('INPUT.TXT', 'r') as input_file:
    N = [int(i) for i in input_file.read().strip().split()]
    N.remove(N[0])
    with open('OUTPUT.TXT', 'w') as output_file:
        list_one = []
        list_two = []
        for i in N:
            if i%2==0:
                list_one.append(i)
            else:
                list_two.append(i)

        output_file.write(' '.join(map(str, list_two)) + '\n')

        output_file.write( ' '.join(map(str,list_one)) + '\n')

        if len(list_one)>len(list_two):
            output_file.write(f'YES\n')
        else:
            output_file.write(f'NO\n')
















        
        








