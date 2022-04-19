class Solution:
    # Graham Scan Method
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def angle(p1, p2, p3):
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            x3, y3 = p3[0], p3[1]
            
            return (y3 - y2)*(x2 - x1) -  (y2-y1)*(x3-x2)
        
        points = sorted(trees)
        lower = []
        upper = []
        for point in points:
            
            while len(lower) >= 2 and angle(lower[-2], lower[-1], point) > 0:
                lower.pop()
                
            while len(upper) >= 2 and angle(upper[-2], upper[-1], point) < 0:
                upper.pop()
            
            lower.append(point)
            upper.append(point)
        
        seen = set()
        newlist = []
        for item in (lower + upper):
             t = tuple(item)
             if t not in seen:
                newlist.append(item)
                seen.add(t)
        
        return newlist
            
            
        
