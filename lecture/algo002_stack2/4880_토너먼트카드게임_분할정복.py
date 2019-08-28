
def battle(card1, card2):
    if data[card1] == data[card2]:
        # 무승부일 경우 인덱스가 작은 사람이 이긴다.
        if card1 < card2:
            return card1
        return card2

    if data[card1] == "1": #가위
        if data[card2] == "2": #바위
            return card2
        else:
            return card1

    if data[card1] == "2":
        if data[card2] == "3":
            return card2
        else:
            return card1

    if data[card1] == "3":
        if data[card2] == "1":
            return card2
        else:
            return card1


def mydiv(s, e):
    # 종료조건
    if s == e:
        return s

    p = (s+e)//2
    card_no1 = mydiv(s, p)
    card_no2 = mydiv(p+1, e)
    winner_card_no = battle(card_no1, card_no2)
    return winner_card_no



TC = int(input())
for tc in range(1, TC+1):
    n = int(input()) # 게임 참여 숫자 개수
    data = list(map(int, input().split())) # 게임 참여 숫자 목록
    winner = mydiv(0, n-1)

