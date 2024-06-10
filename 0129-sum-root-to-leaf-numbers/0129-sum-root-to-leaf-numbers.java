/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum;
    public void divya(TreeNode root,int s)
    {
        if(root==null)
        {
            return;
        }
        if(root.left==null && root.right==null)
        {
            sum+=(s*10+root.val);
            return;
        }
        divya(root.left,s*10+root.val);
        divya(root.right,s*10+root.val);
    }
    public int sumNumbers(TreeNode root) {
        sum=0;
        divya(root,0);
        return sum;
    }
}