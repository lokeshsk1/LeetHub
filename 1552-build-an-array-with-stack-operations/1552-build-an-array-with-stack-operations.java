class Solution {
    public List<String> buildArray(int[] target, int n) {
        
        List<String> res = new ArrayList<String>();

        if(target[0] != 1){
            for(int i=0; i<target[0]-1; i++){
                res.add("Push");
                res.add("Pop");
            }
        }

        res.add("Push");
        

        for(int i=1; i<target.length; i++){
            if(target[i] != target[i-1]){
                int diff = target[i]-target[i-1];
                for(int j=0; j<diff-1; j++){
                    res.add("Push");
                    res.add("Pop");
                }
            }
            res.add("Push");
        }

        return res;
    }
}