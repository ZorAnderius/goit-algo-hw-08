import heapq

def min_order_of_unification(lengths) -> int:
    cables = lengths[:]
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        combined_cost = heapq.heappop(cables) + heapq.heappop(cables)
        total_cost += combined_cost
        heapq.heappush(cables, combined_cost)

    return total_cost


if __name__ == "__main__":
    cables_length = [10, 4, 1, 2]
    min_cost = min_order_of_unification(cables_length)
    print('Найменше значення загальних витрат кабелю становить: ', min_cost)
    