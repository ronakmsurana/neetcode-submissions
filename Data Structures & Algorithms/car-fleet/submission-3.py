class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = []
        for pos,spe in zip(position,speed):
            ans.append([((target - pos)/spe),pos])
        ans.sort(key=lambda x:x[1],reverse = True)
        for i in range(1,len(position)):
            if ans[i][0] < ans[i-1][0]:
                ans[i][0] = ans[i-1][0]
        fin = [i[0] for i in ans]
        return len(set(fin))