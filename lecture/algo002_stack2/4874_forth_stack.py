import sys
sys.stdin = open('4874.txt', 'r')

TC = int(input())

for tc in range(1, TC+1):
    data = list(input().split()) # 공백 나눈 후 리스트로 변환
    n = len(data) # 반복횟수
    stack = []
    result = 0
    errorFlag = False # 예외발생여부

    for i in range(n-1): # 연산식 만큼 반복 # .으로 항상 끝나는 것을 -1로 처리해줘서 에러 처리
        # 숫자이면 스택에 저장
        try:
            if data[i].isdigit(): # 숫자냐?
                stack.append(data[i])
            elif data[i].isdigit() == False: # 숫자가 아니면,
                #print(data[i])
                # 후위표기법 계산 # 마지막_이전 숫자, "연산자" 마지막 숫자
                num2, num1 = int(stack.pop()), int(stack.pop())
                if data[i] == "+":
                    result = num1 + num2
                elif data[i] == "-":
                    result = num1 - num2
                elif data[i] == "*":
                    result = num1 * num2
                elif data[i] == "/":
                    result = num1 // num2
                # 계산결과를 스택에 저장
                stack.append(result)
            # for 끝
        except:
            errorFlag = True

    if errorFlag == False and len(stack) == 1:
        print('#{} {}'.format(tc, stack[0]))
    elif errorFlag == True or len(stack) > 1:
        print('#{} error'.format(tc))




