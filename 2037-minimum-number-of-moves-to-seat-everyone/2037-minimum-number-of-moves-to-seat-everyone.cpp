class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        int a=seats.size();
        int b=students.size();
        sort(seats.begin(),seats.end());
        sort(students.begin(),students.end());
        int r=0;
        for(int i=0;i<a;i++)
        {
            r=r+abs(seats[i]-students[i]);
           
            
        }
        return r;
    }
};