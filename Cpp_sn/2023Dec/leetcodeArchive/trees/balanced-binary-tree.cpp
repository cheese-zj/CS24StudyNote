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

// class Solution {
// public:

//     int f(TreeNode* root){
//         if (root == nullptr) return 0;
//         int r = f(root->right)+1; int l = f(root->left)+1;
//         return std::max(r,l);
//     }

//     bool isBalanced(TreeNode* root) {
//         if (root != nullptr){
//             int df = f(root->right) - f(root->left);
//             if (df > 1 || df < -1 ) return false;
//             if (!isBalanced(root->right) || !isBalanced(root->left)) return false;
//         }
//         return true;
//     }
// };