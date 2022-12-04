class treasure:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.effective = value / weight

K = int(input())   #배낭의 크기
n = int(input())   #아이템의 갯수
arr_weight = list(map(int, input().split()))   #아이템의 크기
arr_value = list(map(int, input().split()))   #아이템의 가치
arr_treasure = []

for i in range(n):
    arr_treasure.append(treasure(arr_value[i], arr_weight[i]))

arr_treasure.sort(key = lambda x : -x.effective)

def fractional(weight, value, W):  #weight는 무게, value는 가치, W는 남은 배낭 용량
    global n
    result = 0
    temp = 0
    for i in range(n):
        if temp + arr_treasure[i].weight > W:
            return result
    temp += arr_treasure[i].weight
    result += arr_treasure[i].value
