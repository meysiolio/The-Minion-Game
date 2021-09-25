def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    L = []
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            #print(f'{string[i:j]} {string.count(string[i:j])}')
            if len(string[i:j]) <= 0 or string[i:j] in L:
                break
            if string[i:j][0] in 'AEIOUaeiou':
                kevin += string.count(string[i:j])
            else:
                stuart += string.count(string[i:j])

            L.append(string[i:j])
        
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif kevin == stuart:
        print(f'TIE in {stuart}')
    else:
        print(f'Stuart {stuart}')

if __name__ == '__main__':
    s = input()
    minion_game(s)