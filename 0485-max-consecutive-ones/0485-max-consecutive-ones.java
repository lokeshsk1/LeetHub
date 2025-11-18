class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        int curr = 0, res = 0;

        for(int i=0; i<nums.length; i++){
            if(nums[i] == 1){
                curr += 1;
            }else{
                curr = 0;
            }
            res = Math.max(res, curr);
        }

        return res;
    }
}