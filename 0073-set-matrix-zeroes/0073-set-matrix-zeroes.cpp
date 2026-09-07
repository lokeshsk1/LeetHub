class Solution {
public:
    void setZeroes(vector<vector<int>>& mat) {
        
        int r = mat.size() , c = mat[0].size();
        int row0 = 1;
        
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(mat[i][j] == 0){
                    if(i==0)
                        row0 = 0;
                    
                    else
                        mat[i][0] = 0;
                    
                    mat[0][j] = 0;
                }
            }
        }

        for(int i=r-1;i>=0;i--){
            for(int j=c-1;j>=0;j--){
                if(i==0){
                    if(row0==0 || mat[0][j] == 0){
                        mat[i][j] = 0;
                    }
                }
                else{
                    if(mat[i][0]==0 || mat[0][j]==0)
                        mat[i][j] = 0;
                }
            }
        }
    }
};