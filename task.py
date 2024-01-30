import heapq
from random import randint

def heap_sort(iterable, descending=False):
    sign = -1 if descending else 1
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    return [sign * heapq.heappop(h) for _ in range(len(h))]

def min_order_of_unification_sorted(lengths):
    sorted_cables = heap_sort(lengths)
    
    total_cost = 0
    while len(sorted_cables) > 1:
        combined_cost= heapq.heappop(sorted_cables) + heapq.heappop(sorted_cables)
        total_cost += combined_cost
        heapq.heappush(sorted_cables, combined_cost)
    return total_cost

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
    cables_length_2 = [randint(1, 30) for _ in range(1000000)]
    min_cost = min_order_of_unification(cables_length)
    min_cost_1 = min_order_of_unification_sorted(cables_length)
    min_cost_2s = min_order_of_unification_sorted(cables_length_2)
    min_cost_2 = min_order_of_unification(cables_length_2)
    print('\nНайменше значення загальних витрат кабелю становить: ', min_cost)
    print('Найменше значення загальних витрат кабелю становить (відсортований): ', min_cost_1)
    print('\nНайменше значення загальних витрат кабелю становить (варіант 2 (відсортований)): ', min_cost_2s)
    print('Найменше значення загальних витрат кабелю становить (варіант 2): ', min_cost_2)
    if min_cost_2 == min_cost_2s:
        print('''\nПопередньо відсортовані довжини та невідсортовані довжини кабелів дають однаковий результат. 
Оскільки ми використовуємо метод heapify для побудови купи. То це дозволяє використовувати купу без попереднього сортування. 
Але лише в тому випадку якщо нам достатньо знайти тільки мінімальне значення, а для визначення як мінімального та макисмального значень, 
доцільно використовувати пірамідальне сортування\n''')
