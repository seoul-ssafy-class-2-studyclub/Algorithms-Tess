'''
7675. 통역사 성경이
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWqPvqoqSLQDFAT_&categoryId=AWqPvqoqSLQDFAT_&categoryType=CODE

'''

char_split = ('!', '?', '.')
m = int(2) #input

for T in range(m):
    n = int(2) #input
#    for T_two in range(2):
    sentences = str('Annyung HaSae Yo! LoL!') # 답은 2 0
    print('d', sentences)

    sentence = []

### ? ! . 알괄 _처리 후 split

    for char in sentences:
        print(char)
        if char in char_split:
            char = char.replace('_')
            sentence += char
        print(sentence)

        #sentence = sentence.split('_')
        #print(sentence)

    count_list = []

    for word in sentence:
        # print(sentence)

        count = 0

        #print(word)
        word = word.split()
        #print('d', str(word))
        for char in word:
            char = list(char)
            #print(char)
            char_lower_temp = char[-1]

            ## capital 다음에는 lower이여야 한다.

            if char[0].isupper() and char_lower_temp.islower():
                count += 1

            #print(count)
        count_list.append(count)
        print(count_list)
        print(f'#{T+1}', end=' ')

        #print(count_list)
        for co in range(len(count_list)-1):
            print(f'{count_list[co]}', end=' ')
            #print(co)
        print('')
        #print(f'{co}', end=' ')