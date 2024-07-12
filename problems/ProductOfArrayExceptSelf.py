
# O(n)
class MySolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        zeros = nums.count(0)
        if zeros >= 2:
            return [0]*n
        elif zeros == 1:
            zero_i = nums.index(0)
            other_nums = nums[:zero_i]+nums[zero_i+1:]
            for i in range(n-1):
                p *= other_nums[i]
            result = [p if i == zero_i else 0 for i in range(n)]
        else:
            for i in range(n):
                p *= nums[i]
            products = [p]*n
            result = [products[i]//nums[i] for i in range(n)]
        return result
        
    
# O(n)
class BestSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result