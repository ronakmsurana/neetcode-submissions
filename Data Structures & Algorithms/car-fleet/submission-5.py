class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spe = list(zip(position,speed))
        pos_spe.sort(key = lambda x:x[0],reverse = True)
        prev = pos_spe[0] = (target - pos_spe[0][0])/pos_spe[0][1]

        for i in range(1,len(pos_spe)):
            cur = (target - pos_spe[i][0])/pos_spe[i][1]
            if cur < prev:
                cur = prev
            prev = cur
            pos_spe[i] = cur
        return len(set(pos_spe))