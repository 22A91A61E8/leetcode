class Solution {
public:
    int longestPalindrome(string s)
    {
        int n = s.length();
        int ans = 0;
        unordered_map<char, int> freq;
        
        // Count the frequency of each character
        for (auto c : s) freq[c]++;
        
        bool isOdd = false;
        
        // Calculate the length of the longest palindrome
        for (auto [c, fr] : freq)
        {
            if (fr % 2 == 0)
            {
                ans += fr; // Add even frequencies entirely
            }
            else
            {
                ans += fr - 1; // Add the largest even number smaller than the frequency
                isOdd = true;  // Indicate there's at least one odd frequency
            }
        }
        
        // If there is at least one character with an odd frequency, we can place one in the center
        if (isOdd)
        {
            ans += 1;
        }
        
        return ans;
    }
};
