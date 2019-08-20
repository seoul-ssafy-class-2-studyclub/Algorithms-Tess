number_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(int(input())):
    tcc, N = tuple(map(str, input().split()))
    N = int(N)
    letter_list = list(map(str, input().split()))
    temp_dict = {}
    for letter in number_list:
        temp_dict[letter] += letter_list.count(letter)
    temp_list = []
    for letter in number_list:
        if letter in temp_dict:
            temp_list.append(temp_dict[letter])
    print('')
    print('{}'.format(tcc))
    for i in range(10):
        for ix in range(temp_list[i]):
            print(number_list[i], end=" ")