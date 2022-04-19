from queue import Queue
class Solution:
    def max_level_sum(self, root):
        q = Queue()
        q.put(root)
        max_sum = float('-inf')
        while not q.empty():
            qL = q.qsize()
            tmp = 0
            while qL:
                item = q.get()
                tmp += item.val
                if item.left:
                    q.put(item.left)
                if item.right:
                    q.put(item.right)
                qL -= 1
            max_sum = max(max_sum, tmp)
        return max_sum