class Solution {
public:
    void sortColors(vector<int>& nums) {
        int temp;
        int a=nums.size();
        for(int i=0;i<a;i++)
        {
          for(int j=0;j<a-1;j++)
          {
              if(nums[j]>nums[j+1])
              {
                temp=nums[j];
                nums[j]=nums[j+1];
                nums[j+1]=temp;
              }
              
          }
        }

    }
};