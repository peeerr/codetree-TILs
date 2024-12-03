# 변수 선언 및 입력
n = int(input())
arr = [0] + list(map(int, input().split()))


def heapify(n, i):
    largest = i                          # 최대 노드가 i번이라고 가정합니다.
    l = i * 2                            # 왼쪽 자식 노드 번호입니다.
    r = i * 2 + 1                        # 오른쪽 자식 노드 번호입니다.

    if l <= n and arr[l] > arr[largest]: # 왼쪽 자식이 크다면, 최대 번호를 수정합니다.
        largest = l
    
    if r <= n and arr[r] > arr[largest]: # 오른쪽 자식이 크다면, 최대 번호를 수정합니다.
        largest = r
    
    if largest != i:                     # 최대 노드가 자식 노드라면
                                         # 해당 자식과 현재 노드를 교환해준 뒤
        arr[i], arr[largest] = arr[largest], arr[i]       
        heapify(n, largest)              # 내려간 위치에서 다시 heapify를 진행합니다.


def heap_sort():
    # 1. max-heap을 만들어 줍니다.
    for i in range(n // 2, 0, -1):    # n / 2번째 원소부터 1번째 원소까지 돌며
        heapify(n, i)                 # heapify 과정을 진행하여 max-heap을 만들어줍니다.

    # 2. 정렬을 진행합니다.
    for i in range(n, 1, -1):         # n을 하나씩 줄여나가며
        arr[1], arr[i] = arr[i], arr[1] # 현재 최댓값과 가장 끝에 있는 노드를 교환해주고
        heapify(i - 1, 1)             # 1번 노드를 기준으로 heapify를 진행하여
                                      # max-heap 상태를 계속 유지해 줍니다.


heap_sort()

for elem in arr[1:]:
    print(elem, end=" ")
    