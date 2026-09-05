/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // same structure and value 
        // test structure by detecting if there is a node, if not then auto false 
        return dfs(p, q);
    }
    // if trees are balanced 
    bool dfs(TreeNode* p, TreeNode* q) {
        // base case 
        if (p == nullptr && q == nullptr) return true; 
        if (p == nullptr || q == nullptr) return false; 
        if (p != nullptr && q != nullptr && p->val != q->val) return false; 
        
        return dfs(p->left, q->left) && dfs(p->right, q->right);
    }
};
