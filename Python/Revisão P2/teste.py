string = str(input())

for i in range(len(string)):
    if string[i] == '0':
        print('1',end='')
    else:
        print(f'{string[i]}',end='')