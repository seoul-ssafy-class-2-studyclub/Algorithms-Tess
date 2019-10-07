'''
6
'''

import sys
sys.stdin = open('1107.txt', 'r')


'''
0부터 9까지 숫자, +와 -가 있다.
+를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고,
-를 누르면 -1된 채널로 이동한다.
 
채널 0에서 -를 누른 경우에는 채널이 변하지 않고,
채널은 무한대 만큼 있다.

채널 100에서 채널 5457로 가기위해 버튼을 최소 몇 번 눌러야할까?
답은 6인데,
6 7 8이 고장난 버튼이라고 한다.
 
0 1 2 3 4 5 6 7 8 9
+ -

0 1 2 3 4 5 9
+ -
'''

N = int(input())
Nn = int(input())
abnormal = list(map(int, input().split()))
normal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operators = ['-', '+']
present = list(set(normal) - set(abnormal))
print(present)

'''
enable_btn_set = {str(x) for x in range(11)}

N = int(input())
break_button_num = int(input())
if(break_button_num == 0):
    pass
else:    
    break_button = set(input().split())
    enable_btn_set -= break_button
    
result = abs(N - 100)
for i in range(1000001):
    is_enable = True
    for div_num in str(i):
        if(div_num not in enable_btn_set):
            is_enable = False
    if(is_enable):
        result = min(result, abs(N - i) + len(str(i)))
        
print(result)
'''