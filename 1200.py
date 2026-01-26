# Question = 1200 ) Minimum Absolute Difference



class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        result = []
        arr.sort()
        difference = float("inf")

        for i in range(len(arr)-1):
            difference = min(difference, arr[i + 1] - arr[i])

        for i in range(len(arr)-1):
            if arr[i + 1] - arr[i] == difference:
                result.append([arr[i], arr[i+1]])
        
        return result
