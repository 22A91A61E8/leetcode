class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int>hei=heights;
        sort(hei.begin(),hei.end());
        int c=0;
        for(int i=0;i<heights.size();i++)
        {
            if(heights[i]!=hei[i])
            {
                c=c+1;
             }
        }
        return c;
    }
};