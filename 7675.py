'''
7675. 통역사 성경이
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWqPvqoqSLQDFAT_&categoryId=AWqPvqoqSLQDFAT_&categoryType=CODE

'''

m = 2
n = 2

a, b, c = '!', '?', '.'

for T in range(int(m)):
    for T_two in range(int(n)):
        sentences = 'Annyung HaSae Yo! LoL!' #str(input())

    if a in sentences:
        sentence = sentences.split(a)
        #analysis_list.append(sentence)

    elif b in sentences:
        sentence = sentences.split(b)
        analysis_list.append(sentence)

    elif c in sentences:
        sentence = sentences.split(c)
        analysis_list.append(sentence)

    #print(sentence)


count_list = []

for word in sentence:

    count = 0

    #print(word)
    word = word.split()
    #print('d', str(word))
    for char in word:
        char = list(char)
        print('넣을게', char)
        #char_lower_temp = char[-1]
        print(char_lower_temp)

        # 첫글자가 upper이고 그다음부터는 1: lower이여야 조건이 성립된다.
        if char[0].isupper() and char_lower_temp.islower():
            count += 1

        #print(count)
    count_list.append(count)

    print(f'#{T}', end=' ')

    #print(count_list)
    for co in range(len(count_list)-1):
        print(f'{count_list[co]}', end=' ')
        #print(co)
    print('')
    #print(f'{co}', end=' ')


