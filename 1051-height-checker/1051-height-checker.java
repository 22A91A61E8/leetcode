class Solution {
    public int heightChecker(int[] heights) {
        int[] hei=heights.clone();
        Arrays.sort(hei);
        int c=0;
        for(int i=0;i<heights.length;i++)
        {
            if(heights[i]!=hei[i])
            {
                c=c+1;
            }
        }
        return c;
    }
}