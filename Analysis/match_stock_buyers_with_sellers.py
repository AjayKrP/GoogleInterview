"""
a way for users to buy and sell stocks
match buyers with the lowest seler (<= buyer's price)
match sellers with the highest buyer (>= seller's price)
"""

arr = [[1, 1, 1, 1, 1],
       [1, 0, 0, 1, 1],
       [1, 0, 0, 1, 1],
       [1, 0, 0, 1, 0]]

res = []


def get_cordinates():
    cordinates = set()
    rows = len(arr)
    cols = len(arr[0])
    for row in range(rows):
        for col in range(cols):
            if arr[row][col] == 0:
                for k in range(row, rows):
                    if arr[k][col] == 1:
                        break
                    cordinates.add((k, col))
    return [min(cordinates), max(cordinates)]


from queue import PriorityQueue

pq = PriorityQueue()
pq.put(('a', 2))
pq.put(('b', 4))
pq.put(('c', 5))
pq.put(('a', 6))

print(pq.queue)