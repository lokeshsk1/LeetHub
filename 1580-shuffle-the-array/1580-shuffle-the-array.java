class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] res = new int[2*n];

        int p1 = 0, p2 = n;

        for(int i=0; i<2*n; i++){
            if(i%2 != 0){
                res[i] = nums[p2];
                p2 += 1;
            }else{
                res[i] = nums[p1];
                p1 += 1;
            }
        }

        return res;
    }
}