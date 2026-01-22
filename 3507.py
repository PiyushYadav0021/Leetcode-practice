./class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ordered = False
        result = 0

        while not ordered:
            ordered = True 
            minimum_value = float("inf")
            minimum_index = -1

            for i in range(len(nums)-1):
                if nums[i+1] + nums[i] < minimum_value:
                    minimum_value = nums[1+i] + nums[i]
                    minimum_index = i
                
                if nums[i+1] < nums[i]:
                    ordered = False
            
            if not ordered :
                nums = nums[0 : minimum_index] + [minimum_value] + nums[minimum_index + 2:]
                result +=1
        return result


![Dashboard](./Images/3507.png)
