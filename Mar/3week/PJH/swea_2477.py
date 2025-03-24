import heapq
T = int(input())
for tc in range(1,T+1):
    N,M,K,A,B = map(int,input().split())
    recept = [0]+list(map(int,input().split()))
    repair = [0]+list(map(int,input().split()))
    tk = [0]+list(map(int,input().split()))

    receipt_status = [-1]*(N+1)
    repair_status = [-1]*(M+1)
    
    pq = []
    for customer_idx in range(1,len(tk)):
        arrival_time = tk[customer_idx]
        in_flag = False
        min_receipt_state = float('inf')
        min_receipt_state_id = -1
        for i in range(1,N+1):
            if arrival_time > receipt_status[i]:
                receipt_status[i] = arrival_time + recept[i] - 1
                heapq.heappush(pq,(arrival_time+recept[i],i,customer_idx))
                in_flag = True
                print(pq)
                print(receipt_status)
                break
            if min_receipt_state > receipt_status[i]:
                min_receipt_state = receipt_status[i]
                min_receipt_state_id = i
        if not in_flag:
            receipt_status[min_receipt_state_id] = min_receipt_state + recept[min_receipt_state_id]
            heapq.heappush(pq,(min_receipt_state+recept[min_receipt_state_id]+1,min_receipt_state_id,customer_idx))
        print(pq)
        print(receipt_status)