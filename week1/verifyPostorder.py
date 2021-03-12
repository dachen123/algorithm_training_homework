#训练场题目8,二叉搜索树的后序遍历序列
#思路 ：1.将后序遍历序列进行排序得到中序序列
#      2.利用中序和后序可得到二叉树的思想，检查这两个序列是否可以顺利构建二叉树，从而得出结论
class Solution:
    def checkTree(self,inorder,inorder_begin,inorder_end,postorder,postorder_begin,postorder_end,result):
        if postorder_begin > postorder_end:
            return 
        node_val = postorder[postorder_end]
        node_idx = inorder_begin
        while node_idx <= inorder_end and inorder[node_idx] != node_val:
            node_idx += 1
        #找不到对应节点，返回False
        if node_idx > inorder_end:
            result['res'] = False
            return 
        left_inorder_begin = inorder_begin
        left_inorder_end = node_idx -1
        right_inorder_begin = node_idx + 1
        right_inorder_end = inorder_end
        left_postorder_begin = postorder_begin
        left_postorder_end = postorder_begin + left_inorder_end - left_inorder_begin
        right_postorder_begin = left_postorder_end + 1
        right_postorder_end = postorder_end - 1
        #切分长度不对，返回False
        if (left_inorder_end - left_inorder_begin != left_postorder_end-left_postorder_begin) or (right_inorder_end - right_inorder_begin != right_postorder_end - right_postorder_begin):
            result['res'] = False
            return
        self.checkTree(inorder,left_inorder_begin,left_inorder_end,postorder,left_postorder_begin,left_postorder_end,result)
        self.checkTree(inorder,right_inorder_begin,right_inorder_end,postorder,right_postorder_begin,right_postorder_end,result)
        return 
    
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        result = {'res':True}
        inorder = sorted(postorder)
        self.checkTree(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,result)
        return result['res']
