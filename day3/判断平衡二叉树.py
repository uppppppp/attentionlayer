class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    def check_height(node):
        if node is None:
            return 0
        
        left_height = check_height(node.left)
        


        if left_height == -1:
            return -1  # 左子树不平衡
        
        right_height = check_height(node.right)
        #print(right_height)
        if right_height == -1:
            return -1  # 右子树不平衡
        print(left_height,right_height)
        height_diff = abs(left_height - right_height)
        if height_diff > 1:
            return -1  # 树不平衡
        
        return max(left_height, right_height) + 1
    
    return check_height(root) != -1

# 创建一个平衡二叉树
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_root.left.left = TreeNode(4)
balanced_root.left.right = TreeNode(5)
balanced_root.right.left = TreeNode(6)
balanced_root.right.right = TreeNode(7)

# 创建一个非平衡二叉树
#         1
#        / \
#       2   3
#      /
#     4
unbalanced_root = TreeNode(1)
unbalanced_root.left = TreeNode(2)
unbalanced_root.right = TreeNode(3)
unbalanced_root.left.left = TreeNode(4)

print("Is the balanced tree balanced?", is_balanced(balanced_root))  # True
print("Is the unbalanced tree balanced?", is_balanced(unbalanced_root))  # False
