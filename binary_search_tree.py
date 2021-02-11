class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST():
    def __init__(self):
        # pointer which points to the root node of the BST
        self.root = None

    # creating a binary tree using a list (using insert_iter as helper method)
    def insert_list(self, data_list):
        root = self.root
        for value in data_list:
            self.insert_iter(value)
        return self.root


    # inserting a node in the BST using iterative approach
    def insert_iter(self, data):
        node = Node(data)

        if not self.root:
            self.root = node
        else:
            tmp = self.root
            parent = None
            while tmp:
                parent = tmp
                if data > tmp.data:
                    tmp = tmp.right
                else:
                    tmp = tmp.left

            if data >= parent.data:
                parent.right = node
            elif data < parent.data:
                parent.left = node
    
        return self.root


    #  inserting a node in BST using recursive approach
    def insert_recur(self, root, data):
        if not root:
            root = Node(data)
        elif data > root.data:
            root.right = self.insert_recur(root.right, data)
        else:
            root.left = self.insert_recur(root.left, data)
        
        return root


    # searching for a specific node in the BST using iterative approach
    def search_iter(self, data):
        flag = False
        tmp = self.root
        while tmp:
            if tmp.data == data:
                flag = True
            elif data > tmp.data:
                tmp = tmp.right
            else:
                tmp = tmp.left
        return flag


    # # searching for a specific node in the BST using recursive approach
    def search_recur(self, root, data):
        if not root:
            return False
        elif data == root.data:
            return True
        elif data > root.data:
            return self.search_recur(root.right, data)
        else:
            return self.search_recur(root.left, data)

    # finding minimum element in the BST iteratively
    def find_min_iter(self):
        root = self.root
        if not root:
            return False
        while root.left:
            root = root.left
        return root.data


    # finding minimum element in the BST recursively
    def find_min_recur(self, root):
        if not root:
            print('Tree is empty...')
        elif not root.left:
            return root.data
        else:
            return self.find_min_recur(root.left) 

    # finding maximum element in the BST iteratively
    def find_max_iter(self, root):
        root = self.root
        if not root:
            return False
        while root.right:
            root = root.right
        return root.data

    # finding maximum element in the BST recursively
    def find_max_recur(self, root):
        if not root:
            print('Tree is empty...')
        elif not root.right:
            return root.data
        else:
            self.find_max_recur(root.right)
    

    # getting the height of the binary search tree
    def get_height(self, root):
        if not root:
            return -1
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return max(left_height, right_height) + 1

    
    # getting the no. of nodes in the binary search tree
    def number_of_nodes(self, root):
        if not root:
            return 0
        return 1 + self.number_of_nodes(root.left) + self.number_of_nodes(root.right)


    # pre-order traversal of BST
    def pre_order(self, root):
        if not root:
            return 
        print(root.data, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)


    # in-order traversal of BST
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.data, end=' ')
        self.in_order(root.right)
    
    # post-order traversal of BST
    def post_order(self, root):
        if not root:
            return 
        self.pre_order(root.left)
        self.pre_order(root.right)
        print(root.data, end=' ')
        
    # level-order traversal of BST
    def level_order(self, root): # same as Breadth First Search using a Queue
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            curr = queue.pop(0)
            print(curr.data, end=' ')

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)




        
            

if __name__ == '__main__':
    tree = BST()

    data = [5, 4, 7, 5, 9, 5, 15, 14, 16, 16, 22, 14, 22, 44, 53, 41, 12, 17]
    root = tree.insert_list(data)

    tree.insert_recur(root, 19)
    tree.insert_recur(root, 33)
    tree.insert_recur(root, 4)

    # tree.in_order(root)
    # print()
    # tree.pre_order(root)
    # print()
    # tree.post_order(root)
    # print()
    # tree.level_order(root)
    # print()



    # result = tree.search_recur(root, 6)
    # print(result)

    # minimun = tree.find_max_iter(root)
    # print(minimun)
    

    # height = tree.get_height(root)
    # print(height)

    # no_of_nodes = tree.number_of_nodes(root)
    # print(no_of_nodes)

