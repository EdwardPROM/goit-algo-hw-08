import heapq

def min_cost_cables(cables):
  heapq.heapify(cables)
  total_cost = 0

  while len(cables) > 1:
    # Видалити два кабелі з найменшою довжиною.
    cable1 = heapq.heappop(cables)
    cable2 = heapq.heappop(cables)
    # Об'єднати їх в один кабель.
    new_cable = cable1 + cable2
    # Додати новий кабель назад до купи.
    heapq.heappush(cables, new_cable)
    # Додати витрати на об'єднання двох кабелів до загальних витрат.
    total_cost += new_cable

  return total_cost
#Тест
cables = [5, 7, 5, 9, 15]
total_cost = min_cost_cables(cables)
print(f"Витрати на з'єднання кабелів: {total_cost}")
