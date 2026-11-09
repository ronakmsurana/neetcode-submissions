class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position = list(zip(position,speed))
        position.sort(key = lambda x:x[0],reverse = True)
        prev = position[0] = (target - position[0][0])/position[0][1]

        for i in range(1,len(position)):
            cur = (target - position[i][0])/position[i][1]
            if cur < prev:
                cur = prev
            prev = cur
            position[i] = cur
        return len(set(position))