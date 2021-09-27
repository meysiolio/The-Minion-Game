def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    L = []
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
        
            if len(string[i:j]) <= 0 or string[i:j] in L:
                break

            print(f'{string[i:j]} {count_substring(string,string[i:j])}')

            if string[i:j][0] in 'AEIOUaeiou':
                kevin += count_substring(string,string[i:j])
            else:
                stuart += count_substring(string,string[i:j])

            L.append(string[i:j])
        
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif kevin == stuart:
        print(f'Draw in {stuart}')
    else:
        print(f'Stuart {stuart} {kevin}')

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    s = input()
    minion_game(s)