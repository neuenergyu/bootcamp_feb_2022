
prime = 997

max_other = 999

def separate(giveNumber):
    string_num = str(giveNumber)
    mapObject = map(int, string_num)
    separate_digit_list = list(mapObject)
    return separate_digit_list


def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]

is_it = False

while not(is_it):
    N = max_other * prime
    
    N_list = separate(N)
    N_list = [str(x) for x in N_list]
    
    
    is_it = palindrome(''.join(N_list))
    print(max_other, N, is_it)
    
    max_other = max_other - 1
    
print('el mayor palíndrommo es {}, y se hace como {} x {}'.format(N, max_other+1, 997))

