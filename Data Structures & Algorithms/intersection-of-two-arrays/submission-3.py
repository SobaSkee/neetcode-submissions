class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # [1,1,2,2] and [2,2]
        if len(nums1) > len(nums2):
            search = nums1
            shorter = nums2
        else:
            search = nums2
            shorter = nums1
        search.sort()
        res = []
        seen = set()
        l = 0
        r = len(search)-1
        for num in shorter:
            if num in seen:
                continue
            while l <= r:
                mid = (r+l)//2
                if search[mid] == num:
                    res.append(num)
                    seen.add(num)
                    break
                elif search[mid] > num:
                    r = mid-1
                else:
                    l = mid+1         
            l = 0
            r = len(search)-1
        return res

            