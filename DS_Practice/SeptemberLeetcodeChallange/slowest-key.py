class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = {}
        for i in range(len(keysPressed)):
            if i == 0:
                time[keysPressed[i]] = releaseTimes[i]
                pass
            
            if keysPressed[i] not in time: 
                time[keysPressed[i]] = releaseTimes[i] - releaseTimes[i-1]
            else:
                diff = releaseTimes[i] - releaseTimes[i-1]
                if diff > time[keysPressed[i]]:
                    time[keysPressed[i]] = diff
            time = dict(sorted(time.items(), reverse=True))
            time = dict(sorted(time.items(), key=lambda x:x[1], reverse=True))
            
            print(time)
        return list(time.keys())[0]

            
