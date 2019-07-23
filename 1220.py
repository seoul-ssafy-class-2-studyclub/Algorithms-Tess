
'''
# 리스트내의 리스트 만들기
'''
for T in range(1, 11): # T case는 총 10개다.
    n = int(input()) # 입력 받는 크기 -> 이만큼으로 사각형을 만들어주어야 한다.
    new_lists = [] # 받은 row들을 집어넣을 빈 테이블
    count = 0 # count할 기본 값

    for t in range(n): # 100x100의 리스트 내의 리스트를 만든다.
        new_lists.append(list(map(int, input().split())))

    print(new_lists)
'''
# 교착상태 만들기
# 우리가 count해야하는 부분은 세로, 이를 계산하기 위해서 세로줄을 계산한다
우리가 필요한건 

1이 앞에있다면 
2가 뒤에 있어야 한다는 것이고,

1앞에 1이있다면 뒤돌아가며
2가 있다면 count를 해주면 된다.
'''
    for i in range(n):
        for j in range(n):
            if new_lists[j][i] == 1:
                for d in range(j+1, n):
                    if new_lists[d][i] == 1:
                        break
                    elif new_lists[d][i] == 2:
                        count += 1
    print(f'#{T} {count}')














'''
    for i in range(n):  # 상위 리스트의 인덱스
        second_new_list = []

        for j in range(n):  # 하위 리스트의 인덱스
            second_new_list.append(new_lists[j][i]) # j가 한번 돌때 i가 100번 도니까 가로리스트가 생성된다.
    print(second_new_list)  # 1케이스에 해당하는 가로리스트 완성, 10번 반복한걸 원할땐 해당 for문 바깥으로 간다.


가로로 만든 리스트에서 필요없는 0을 정제한다.
'''

'''
# 그러면 조건은
# 리스트 내의 리스트 (항상 다음 인덱스인 리스트) 후의 리스트 같은 인덱스 상에서
# 1,2 여야 한다.
# 0~100 idx

# 가로 리스트 생성



        while 0 in second_new_list: # 0은 필요 없으므로 삭제
            second_new_list.remove(0)

        #print(second_new_list)  #가로 리스트 하나에서 0을 제외

        while second_new_list[0] == 2: # 끝의 2는 필요없으므로 삭제
            second_new_list.remove(2)

        # while second_new_list[:] == 1:
        #     second_new_list.pop()

        print(second_new_list)

'''


'''
        for idec in range(len(second_new_list)+1):
            try: #앞이 1이고 그 뒤가 2라면 1을 더해준다.
                if second_new_list[idec] == 1 and second_new_list[idec+1] == 2:
                    count += 1
            except IndexError:
                continue
    print(count)


#1뒤에 2가 있을

'''




'''
***
del 함수사용해보기
***
#보이어모어

1, 2 pattern
'''
'''

def bm_algo(text, pattern):
    i = len(text)
    j = len(pattern)

    text_index = j - 1
    pattern_index = j - 1

    while text_index < i:
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                return text_index
            else:
                text_index -= 1
                pattern_index -= 1
        else:
            while pattern_index >= 0:
                if text[text_index] == pattern[pattern_index]:
                    text_index = text_index + j - (pattern_index + 1)
                    pattern_index = j - 1
                    break
                else:
                    pattern_index -= 1
            if pattern_index == -1:
                text_index = text_index + j
                pattern_index = j - 1
    return '패턴이 존재하지 않습니다.
'''


''' 잠시 hold
for idxe in range(100): # 상위 리스트의 인덱스
    count = 0

    for idx in range(100): # 하위 리스트의 인덱스
        try:
            if new_lists[idxe][idx] == 1:
                if new_lists[idxe+1][idx] == 2:
                    count += 1
                    print(count)

            elif new_lists[idxe][idx] == 2:
                if new_lists[idxe+1][idx] == 1:
                    count += 1
                    print(count)

    print(count)

            #count += count

        except IndexError:
            continue

print(count)
'''
