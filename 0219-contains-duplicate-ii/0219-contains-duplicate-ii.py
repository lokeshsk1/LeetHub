class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        st = set()

        for i in range(len(nums)):

            if nums[i] in st:
                return True

            st.add(nums[i])
            
            if len(st) > k:
                st.remove(nums[i-k])

        return False


