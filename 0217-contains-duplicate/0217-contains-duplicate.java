class Solution {
    public boolean containsDuplicate(int[] nums) {

        HashSet<Integer> hashset = new HashSet<>();

        for(int i=0; i<nums.length; i++){
            hashset.add(nums[i]);
        }

        return nums.length != hashset.size();
        
    }
}