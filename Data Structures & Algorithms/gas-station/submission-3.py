class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i+1
        return start


        # gas = [1, 2, 3, 4]
        # cost= [2, 2, 4, 1]
        # diff= [-1, 0, -1, 3]                
            
            
