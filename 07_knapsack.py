class Item:
  def __init__(self, profit, weight):
    self.profit = profit
    self.weight = weight
    self.ratio = profit / weight

def Knapsack(items, capacity):
  items.sort(key = lambda x: x.ratio, reverse = True)

  prof = 0
  rem = capacity

  for item in items:
    if rem <= 0:
      break

    if rem >= item.weight:
      prof += item.profit
      rem -= item.weight
    else:
      a = rem / item.weight
      prof += a * item.profit
      break

  return prof

Items = [Item(60,10), Item(100,20), Item(120,30)]
Capacity = 50

max_profit = Knapsack(Items, Capacity)
print("Maximum Profit: ",max_profit )