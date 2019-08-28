
# queue 삽입 구현
myqueue = []

def enQueue(item):
    # 함수 내에서 쓰는 변수는 꼭 다른 이름(로컬변수)으로 사용하기!
    # . 을 사용하기때문에 myqueue 자체에 쓰는게 아니라 주소값을 가져와서 사용하기때문에 global선언 없이 사용가
    myqueue.append(item)

def deQueue():
    return myqueue.pop(0) # 처음에 있는 것을 pop한다.

enQueue(1)
enQueue(2)
enQueue(3)
print("myqueue", myqueue)

# queue 삭제 구현
# 첫번째 요소 삭제
print(deQueue())
print(deQueue())
print(deQueue())
print("myqueue", myqueue)
print('ok')

