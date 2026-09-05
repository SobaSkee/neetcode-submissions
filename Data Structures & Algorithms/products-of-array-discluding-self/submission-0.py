class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        res = []

        # build prefix
        rolling_sum = nums[0]
        prefix.append(rolling_sum)
        for i in range(1, len(nums)):
            rolling_sum *= nums[i]
            prefix.append(rolling_sum)

        rolling_sum = nums[-1]
        postfix.append(rolling_sum)
        for i in range(len(nums)-2, -1, -1):
            rolling_sum *= nums[i]
            postfix.append(rolling_sum)
        postfix = list(reversed(postfix))

        for i in range(len(nums)):
            if i == 0:
                product = 1 * postfix[i+1]
            elif i == len(nums)-1:
                product = prefix[i-1] * 1
            else:
                product = prefix[i-1] * postfix[i+1]
            res.append(product)
        print("prefix: ", prefix)
        print("postfix: ", postfix)
        return res

# e.g. prefix for [1, 2, 3, 4] is [1, 2, 6, 24]
#       postfix [1, 2, 3, 4] is []