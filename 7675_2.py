'''
7675. 통역사 성경이
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWqPvqoqSLQDFAT_&categoryId=AWqPvqoqSLQDFAT_&categoryType=CODE

'''

m = int(input())

a, b, c = '!', '?', '.'

for T in range(m):
    n = int(input())
#    for T_two in range(2):
    sentences = str(input())
    print('d', sentences)

    if a in sentences:
        sentence = sentences.split(a)
        #analysis_list.append(sentence)

    if b in sentences:
        sentence = sentences.split(b)
        #analysis_list.append(sentence)

    if c in sentences:  ### 얘까지 못감
        sentence = sentences.split(c)
        #analysis_list.append(sentence)

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