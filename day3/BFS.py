class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_tree(root):
    if not root:
        return

    queue = []  # 创建一个队列用于BFS
    queue.append(root)
    cur = []
    while queue:
        node = queue.pop(0)  # 出队
        #print(node.value, end=' ')  # 访问节点
        cur.append(node.value)

        # 将左右子节点入队
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(cur)
    return cur
# 创建一个简单的二叉树
#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 执行树的BFS遍历
bfs_tree(root)
